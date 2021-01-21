# Room
https://tryhackme.com/room/johntheripper0

# Task 1 - John who?
John the Ripper is a hash cracking tool that uses brute forcing with a dictionary.

A hash is a one way function that takes a piece of input of any length and coverts it to a fixed length output.  The algorithm that performs this operation can be MD5 or SHA1, among others.  Changing one character in the input results in a completely different hash output.

* MD5 hash examples
    ```
    echo test123 | md5sum
    4a251a2ef9bbf4ccc35f97aba2c9cbda  -

    echo test124 | md5sum
    0af9cdec30bc6e4e42178a3918b0fbe9  -

    echo test124asdofiuwer982374raspdfoisdfkjwerjh23498asdpofiuasdfkl | md5sum
    ca158883c73432f3ea520ce7e1920eaa  -
    ```

# Task 2 - Setup
There is a standard core distribution of John.  A popular community edition is called Jumbo John.

* Ubuntu
    * sudo apt install john
* Windows
    * 64 : https://www.openwall.com/john/k/john-1.9.0-jumbo-1-win64.zip
    * 32 : https://www.openwall.com/john/k/john-1.9.0-jumbo-1-win32.zip

# Task 3 - Wordlists
Dictionary attacks require wordlists.  There are many available, you can also create your own.

* Parrot, Kali, AttackBox
    * /usr/share/wordlists
* SecLists
    * https://github.com/danielmiessler/SecLists

# Task 4 - Cracking Basic Hashes
