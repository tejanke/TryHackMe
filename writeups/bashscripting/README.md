# Room
https://tryhackme.com/room/bashscripting

# Task 1 - Intro
Bash is a scripting language that runs in the terminal.  Shell scripts are a sequence of bash commands.
* Reference: https://devhints.io/bash

# Task 2 - Simple Bash Script
A simple script
* Bash scripts always start with #!/bin/bash
    * This tells the shell your script runs with bash
* Echo is used to output text on the screen
* You can use Linux commands inside your script
* To run your script, you must make it executable
    * chmod +x script.sh
* Run the script by prefixing it with ./

# Task 3 - Variables
A variable is a temporary storage space in memory to store a piece of data
* Variables have a name, assignment operator, and a value
    * game="poker"
* To use your variable, call the name of it with a $ in front
    * $game
* You can debug your script by sectioning off your script with set -x and set +x
    ```
    #!/bin/bash
    echo "begin"

    set -x
    echo "test"
    set +x

    echo "end"
    ```
* Then execute your script with bash -x ./script.sh
* You can use multiple variables in an echo statement
    ```
    cat test2.sh 
    #!/bin/bash
    year=2044
    day="Monday"
    echo "The year is $year and the day is $day"

    ./test2.sh 
    The year is 2044 and the day is Monday
    ```
# Task 4 - Parameters
You can modify the function of your script with parameters from the CLI
* Parameters provided to your script from the command line start with $ followed by a number
    ```
    cat test3.sh
    #!/bin/bash
    name=$1
    age=$2
    echo "Your name is $name and your age is $age"

    ./test3.sh bob 31
    Your name is bob and your age is 31
    ```
* Instead of supplying parameters to the script CLI, you can also prompt for them with read
    ```
    cat test4.sh 
    #!/bin/bash
    echo "Enter your name"
    read name
    echo "Your name is $name"

    ./test4.sh 
    Enter your name
    bob
    Your name is bob
    ```
# Task 5 - Arrays
Arrays can store multiple pieces of data in one variable
* Bash arrays use 0 indexing - they start at 0
* Example array
    ```
    fruit=('apple' 'orange' 'lemon')
    ```
* Echo all elements in the array
    ```
    echo "${fruit[@]}"
    ```
    * @ means all data in the array
* Echo the 2nd element in the array
    ```
    echo "${fruit[1]}"
    ```
* Remove an element in the array
    ```
    unset fruit[2]
    ```
* Add an element to the array
    ```
    fruit[2]='melon'
    ```
# Task 6 - Conditionals
Code that takes into consideration a certain condition
* If statements
    ```
    if [ ]
    then
    else
    fi
    ```
* Operators
    ```
    -eq
    -ne
    -gt
    -lt
    -ge
    ```
* Flags
    ```
    -f
    -w
    -r
    -d
    ```
# Task 7 - Further Reading
* https://www.codewars.com/
* https://www.hackerrank.com/