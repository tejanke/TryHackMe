# Room
https://tryhackme.com/room/burpsuiteintruder

# Task 1 - Intro
Intro

# Task 2 - What is intruder?
* Intruder is Burp's fuzzing tool
* Similar to wfuzz or ffuf

# Task 3 - Positions
* Positions tells intruder where to insert payloads

# Task 4 - Attack Types
* Sniper
* Battering Ram
* Pitchfork
* Cluster bomb

# Task 5 - Sniper
* Sniper is the most common attack type
* It accepts 1 payload set when conducting an attack and is good for single parameter targets

# Task 6 - Battering Ram
* Like sniper but puts the same payload in every position rather than each position in turn

# Task 7 - Pitchfork
* Like having numerous snipers running simultaneously
* Pitchfork uses one payload set per position up to a max of 20

# Task 8 - Clusterbomb
* Like Pitchfork but iterates through each payload set individually
* Ensures every possible combination of payload is tested

# Task 9 - Payloads
* The Payloads tab allows you to add word lists, manual items, and manipulate the processing of your attack data

# Task 10 - Practical Example
* Download the wordlist zip on the attack VM.  Unzip it.  Load Burp, Open Browser, Submit a bogus login request.  Send the request to intruder.  Load the usernames wordlist for the simple list payload 1 and the password wordlist for simple list payload 2.  Change the attack type to Pitchfork, start attack.  Save the creds.

# Task 11 - Challenge
* Using the saved creds from the last challenge, login to the support site.  Now that you have an authenticated session with cookie, browse to the first support ticket.  Send this request to intruder and perform a sniper attack to fuzz the ticket number in the GET request.  You'll use the numbers payload with a sequence from 1 to 100.  Find the flag in the response.

# Task 12 - CSRF Token Bypass
CSRF Token Bypass

# Task 13 - Conclusion
Conclusion