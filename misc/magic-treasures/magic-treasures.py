#!/usr/bin/python3
# pip3 install -r requirements.txt
#
# a basic file signature changer
#
# todo : 
# - multiple signatures, extensions in the same cell
# - refactor

import requests
import pandas as pd
import shutil
import binascii

signature_url = 'https://en.wikipedia.org/wiki/List_of_file_signatures'

print("Fetching Magic Numbers...")
r = requests.get(signature_url)
print(r)

df_list = pd.read_html(r.text)
df = df_list[0]
print(df)


search = ""
while search.lower() != "!q":
    search = input("Type the file extension to search for (without a .), !w to write, or !q to quit: ")
    if search.lower() == "!q":
        exit
    if search.lower() == "!w":
        i = input("Type the search result index to write that magic number, !s to search, or !q to quit: ")
        if i.lower() == "!q":
            exit
        if i.lower() == "!s":
            pass
        else:
            filename = input("Type the existing filename to insert the magic number, !s to search, or !q to quit: ")
            if filename.lower() == "!q":
                exit
            if filename.lower() == "!s":
                pass
            else:
                backup = filename + ".magic"
                #print(i)
                #print(df.iloc[int(i)])
                #print(df.iloc[int(i)][1])
                sig = df.iloc[int(i)][3]
                magic = df.iloc[int(i)][1]
                magic_number = []

                for h in df.iloc[int(i)][0].split(" "):
                    magic_number.append(h)
                print(magic_number)
                shutil.copyfile(filename, backup)
                
                with open(backup, 'wb') as f:
                    for n in magic_number:
                        f.write(binascii.unhexlify(n))

                with open(filename, 'r') as r:
                    out = r.readlines()

                with open(backup, 'a') as q:
                    for line in out:
                        q.write(line)
                
                print("Wrote [{}] signature [{}] to [{}]".format(sig, magic, backup))
    else:
        print(df.loc[df['Filename extension'].str.contains(search.lower(), na=False)])
