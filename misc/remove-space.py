#!/usr/bin/python3

with open("input.txt", "r") as i:
    test_string = i.read()

out_string = test_string.strip(' \t\n\r').replace(' ','').replace('\r\n', '').replace('\n', '')
print(out_string)

with open("output.txt","w") as f:
    f.write(out_string)