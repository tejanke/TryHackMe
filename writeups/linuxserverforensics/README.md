# Room
https://tryhackme.com/room/linuxserverforensics

# Task 1 - Deploy VM
Deploy VM

# Task 2 - Apache log analysis
The Apache access log keeps a history of source address, response code and length, user-agent, and others.  The log is stored in /var/log/apache2

# Task 3 - Web server analysis
Review the Apache access log and answer questions based on the contents

# Task 4 - Persistence mechanisms 1
Evidence of persistence includes
* cron jobs
* abnormal services
* updates to .bashrc
* abnormal kernel modules
* SSH keys

Review the cron file at /etc/crontab

# Task 5 - User Accounts
* /etc/passwd - contains names of most accounts on the system
* /etc/shadow - contains names and password hashes, strict permissions

# Task 6 - Deploy VM
Deploy

# Task 7 - Apache Log Analysis
Review Apache log file and answer questions.  You can process binary files with grep -a

# Task 8 - Persistence Mechanisms
Search for authorized_keys files

sudo find / -name "*keys" -type f 2>/dev/null

# Task 9 - Program Execution History
* bash_history - history of commands run in bash
* auth.log - contains a history of all commands run using sudo
* history.log - history of all tasks performed using apt

