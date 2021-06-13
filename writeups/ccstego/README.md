# Room
https://tryhackme.com/room/ccstego

# Task 1 - Intro
Steganography is the art of concealing something inside something else

# Task 2 - Steghide
Steghide is a famous steganongraphy tool that allows you to hide a message inside an image, among other things

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