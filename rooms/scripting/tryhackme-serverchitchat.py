import os
import socket
import sys
import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)


server_ip = "change_me"
request = "hello"
next_port = 4000
pms = 0.2

def decrypt(key, associated_data, iv, ciphertext, tag):
    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
        backend=default_backend()
    ).decryptor()

    decryptor.authenticate_additional_data(associated_data)

    return decryptor.update(ciphertext) + decryptor.finalize()

# Connect
print("start")
time.sleep(pms)
b = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (server_ip, next_port)

b.sendto(request.encode('utf-8'), server_address)
data, server = b.recvfrom(4096)
print("-" * 20, len(data))
print(data.decode('utf-8'))

# Key and IV
next_request = "ready"
b.sendto(next_request.encode('utf-8'), server_address)
data, server = b.recvfrom(4096)
print("-" * 20, len(data))
print(data)
key = data.split(b' ')[0]
key = key.split(b'key:')[1]
iv = data.split(b' ')[1]
iv = iv.split(b'iv:')[1]

# Ciphertext and Tag
more_tags = 0
while more_tags < 12:
    # Ciphertext
    next_request = "final"
    b.sendto(next_request.encode('utf-8'), server_address)
    data, server = b.recvfrom(4096)
    print("-" * 20, len(data))
    print(data)
    ct = data
    # Tag
    next_request = "final"
    b.sendto(next_request.encode('utf-8'), server_address)
    data, server = b.recvfrom(4096)
    print("-" * 20, len(data))
    print(data)
    tg = data
    more_tags += 1

    flag = decrypt(
        key,
        b"",
        iv,
        ct,
        tg
    )

    print(flag.decode('utf-8'))

b.close()
print("end")
