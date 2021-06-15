# Room
https://tryhackme.com/room/ccstego

# Task 1 - Intro
Steganography is the art of concealing something inside something else

# Task 2 - Steghide
Steghide is a famous steganongraphy tool that allows you to hide a message inside a jpg image, among other things

Install
* sudo apt install steghide

Useful arguments
* embed - allows you to embed data
* -ef - set the file to embed 
* -cf - set a cover file
* -p - set a password for the cover file
* extract - allows you to extract data from a file
* -sf - file you want to extract data from

Example
```
steghide extract -sf filename
```

# Task 3 - zsteg
zsteg is like steghide, but it is for png and bmp files

Install
* gem install zsteg

Example
```
zsteg png1.png -v
```

# Task 4 - exiftool
exiftool allows you to view and edit image metadata

Install
* sudo apt install exiftool

Example
```
exiftool jpeg3.jpeg
```

# Task 5 - stegoveritas
stegoveritas supports about every image file and is able to extract data

Install
* pip3 install stegoveritas

Example
```
stegoveritas -steghide filename
```