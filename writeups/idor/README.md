# Room
https://tryhackme.com/room/idor

# Task 1 - What is an IDOR?
1. What is an IDOR
   * IDOR = Insecure Direct Object Reference
   * access control vulnerability

# Task 2 - IDOR Example
Explore the IDOR vulnerable web site and try changing the user_id parameter

# Task 3 - Finding IDORs in encoded IDs
Base64 is a common encoding type

https://www.base64encode.org/

https://www.base64decode.org/

# Task 4 - Finding IDORs in hashed IDs
IDs may be hashed with algorithms like MD5 or SHA, crack them using

https://crackstation.net/

# Task 5 - Finding IDORs in unpredictable IDs
A common IDOR detection practice is to create two accounts and swap the ID numbers between them to look for direct access

# Task 6 - Where to locate IDORs
You can use parameter mining to discover dev functions that may have been pushed to production

# Task 7 - Practical Example
Start the VM and navigate to the web page in the challenge.  Create a new user account and login.  Once logged in note that your username and email are filled into the profile boxes.  Turn on developer tools in the browser and reload the page.  Scan the output shown in the network tab of developer tools and find an API call that retrieves the information for your profile.  Copy the URL of the API call into the browser address bar and fuzz a few different IDs to see what you find.  Answer the questions as presented.