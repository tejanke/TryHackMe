#!/usr/bin/python3

import zipfile
import os
import exiftool

# Set filename and output dir
filename = "final-final-compressed.zip"
out_dir = filename.split(".")[0]

# Create output dir if it doesn't exist
if os.path.isdir(out_dir) == False:
    os.mkdir(out_dir)

# Create unzip function

def unzip_file(filename, outdir):
    with zipfile.ZipFile(filename, 'r') as zip_file:
        zip_file.extractall(out_dir)
    return

# Unzip main zip file to output dir
unzip_file(filename, out_dir)

# For each zip file in the outpdir, unzip it in the output dir
for filename in os.listdir(out_dir):
    print(filename)
    filename = out_dir + "/" + filename
    print(filename)
    if ".zip" in filename:
        unzip_file(filename, out_dir)

# Counter the number of non-zip files in the output dir
file_counter = 0
txt_files = []
for filename in os.listdir(out_dir):
    if ".zip" not in filename:
        print(filename)
        file_counter += 1
        txt_files.append(out_dir + "/" + filename)
print("Total files = {}".format(file_counter))
print(txt_files)

# Read each non-zip file searching for the text "Version: 1.1" in metadata and
# the password in each plaintext file
version_counter = 0
password_file = ""
with exiftool.ExifTool() as et:
    metadata = et.get_metadata_batch(txt_files)
    for d in metadata:
        #print(d)
        if "XMP:Version" in d:
            print(d)
            version_counter += 1
            print(d['XMP:Version'])
        if d['File:MIMEType'] == "text/plain":
            with open(out_dir + "/" + d['File:FileName']) as f:
                lines = f.readlines()
                for line in lines:
                    if "pass" in line.lower():
                        password_file = d['File:FileName']
print("Total files with Version 1.1 = {}".format(version_counter))
print("Password file = {}".format(password_file))