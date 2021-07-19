# Room
https://tryhackme.com/room/rpsublist3r

# Task 1 - Intro
sublist3r is a python script that allows quick and easy recon to discover subdomains

* Resources
  * https://dnsdumpster.com/
  * https://github.com/aboul3la/Sublist3r

# Task 2 - Installation
* Install sublist3r
  * https://github.com/aboul3la/Sublist3r
```
$ cd /opt

/opt$ sudo git clone https://github.com/aboul3la/Sublist3r

Cloning into 'Sublist3r'...
remote: Enumerating objects: 383, done.
remote: Total 383 (delta 0), reused 0 (delta 0), pack-reused 383
Receiving objects: 100% (383/383), 1.12 MiB | 3.84 MiB/s, done.
Resolving deltas: 100% (212/212), done.

/opt$ cd Sublist3r/

/opt/Sublist3r$ pip3 install -r requirements.txt 
Collecting argparse
  Using cached argparse-1.4.0-py2.py3-none-any.whl (23 kB)
Requirement already satisfied: dnspython in /usr/lib/python3/dist-packages (from -r requirements.txt (line 2)) (2.0.0)
Requirement already satisfied: requests in /usr/local/lib/python3.9/dist-packages (from -r requirements.txt (line 3)) (2.20.0)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /usr/local/lib/python3.9/dist-packages (from requests->-r requirements.txt (line 3)) (3.0.4)
Requirement already satisfied: certifi>=2017.4.17 in /usr/lib/python3/dist-packages (from requests->-r requirements.txt (line 3)) (2020.6.20)
Requirement already satisfied: urllib3<1.25,>=1.21.1 in /usr/local/lib/python3.9/dist-packages (from requests->-r requirements.txt (line 3)) (1.24.3)
Requirement already satisfied: idna<2.8,>=2.5 in /usr/local/lib/python3.9/dist-packages (from requests->-r requirements.txt (line 3)) (2.7)
Installing collected packages: argparse
Successfully installed argparse-1.4.0
```

# Task 3 - Useful switches
Useful switches

```
python sublist3r.py -h
usage: sublist3r.py [-h] -d DOMAIN [-b [BRUTEFORCE]] [-p PORTS] [-v [VERBOSE]]
                    [-t THREADS] [-e ENGINES] [-o OUTPUT] [-n]

OPTIONS:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Domain name to enumerate it's subdomains
  -b [BRUTEFORCE], --bruteforce [BRUTEFORCE]
                        Enable the subbrute bruteforce module
  -p PORTS, --ports PORTS
                        Scan the found subdomains against specified tcp ports
  -v [VERBOSE], --verbose [VERBOSE]
                        Enable Verbosity and display results in realtime
  -t THREADS, --threads THREADS
                        Number of threads to use for subbrute bruteforce
  -e ENGINES, --engines ENGINES
                        Specify a comma-separated list of search engines
  -o OUTPUT, --output OUTPUT
                        Save the results to text file
  -n, --no-color        Output without color

Example: python sublist3r.py -d google.com
```

# Task 4 - Practical
Use sublist3r or dnsdumpster to answer questions in the practical