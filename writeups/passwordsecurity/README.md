# Room
https://tryhackme.com/room/passwordsecurity

# Task 1 - Credit
This room material is largely based on slides made by Dr. Ruben Niederhagen and Dr. Andreas Hülsing from the Technical University of Eindhoven

# Task 2 - Intro
Passwords are one of three forms of authentication, what you know.  The others are what you are and what you have.  Passwords were first used in 1961 at MIT.  When passwords are securely stored, they are saved as a hash.  There are two types of attacks against passwords, online and offline.  Online attacks are easily mitigated with timeouts.  Offline attacks are better from the perspective of the attacker and are mostly impossible to defend against

# Task 3 - Good Passwords
Password complexity and not reusing it is important.  Linux has a password generator called pwgen

# Task 4 - Password Attacks
Attack types
* Guessing - guess a password using known attributes of the target
* Dictionary Attack - use a common wordlist like rockyou.txt
* Rainbow Tables - use pre-computed hashes of already brute forced passwords 
* Brute-Force - process all combinations of a-z A-Z 0-9 symbols, etc

# Task 5 - Password Storage and Defense
Storage
* Plain text - this is the worst possible storage method
* Hashed - hashing, or better salted hashing is the preferred method of storage

Hashes for the same password with different users are the same, salted hashes for the same password with different users are different