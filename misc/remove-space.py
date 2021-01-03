#!/usr/bin/python3

# Populate input.txt with a text blob, save, run the script, all spaces, new lines, etc removed and the 
# the result is saved to output.txt

with open("input.txt", "r") as i:
    test_string = i.read()

out_string = test_string.strip(' \t\n\r').replace(' ','').replace('\r\n', '').replace('\n', '')
print(out_string)

with open("output.txt","w") as f:
    f.write(out_string)