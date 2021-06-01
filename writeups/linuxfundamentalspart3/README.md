# Room
https://tryhackme.com/room/linuxfundamentalspart3

# Task 1 - Intro
Course Intro

# Task 2 - Deploy
Deploy

# Task 3 - Text editors
Popular text editors
* nano
* vim

# Task 4 - Useful utilities
Useful utilities
* wget - download files
* scp - secure copy files
* curl - receive web page in text form from CLI
* python -m http.server - start a web server with Python

# Task 5 - Processes 101
Process information
* ps - view active processes for the current user
* ps aux - view active processes for all users
* top - view real time statistics about active processes
* kill - terminate a process using its PID
  * SIGTERM - cleanly kill a process
  * SIGKILL - kill the process with no cleanup
  * SIGSTOP - stop / suspend the process
* systemd is one of the first processes to start.  Any other program that wants to start will spawn as a child of systemd
* you can use the systemctl command to start, stop, enable, and disable processes
* processes can run in two states, foreground and background
* & is used to put a process in the background
* ctrl + z can also put a process in the background
* fg will bring a backgrounded process back into use on the terminal

# Task 6 - Automation
Automation
* cron
* crontab - a special file with formatting recognized by cron
  * can be edited with crontab -e

# Task 7 - Package Management
Package Management
* apt
* /etc/apt
* add-apt-repository
* dpkg

# Task 8 - System Logs
System Logs
* /var/log
* access.log
* error.log

# Task 9 - Conclusion
Conclusion