# Room
https://tryhackme.com/room/catregex

# Task 1 - Intro
Regular expressions are patterns of text that you define to search documents and match what you are looking for

Tool
* https://regexr.com/

# Task 2 - Charsets
A charset is defined by enclosing characters in square brackets

Examples
* [abc] will match a, b, and c
* [abc]zz will match azz, bzz, and czz
* [a-zA-Z] will match any single letter upper or lowercase

# Task 3 - Wildcards
Wildcards are used to match single characters.  You can use the question mark to specify an optional character.  In order to match for a period you must escape it with a \

Examples
* .at will match Cat, fat, hat, rat
* cat\.xyz will match cat.xyz
* abc? will match ab and abc

# Task 4 - Metacharacters and repetitions
Meacharacters allow you to match big character sets

Examples
* \d matches a digit
* \D matches a non digit
* \w matches an alphanumeric character
* \W matches a non alphanumeric character

# Task 5 - Starts with ends with
Searching for a pattern in the beginning or the end of a line.  You can also group matches together using ( and )

Examples
* ^ - starts with
* $ - ends with
* (day|night) - matches day or night

# Task 6 - FIN