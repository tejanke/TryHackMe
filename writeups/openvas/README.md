# Room
https://tryhackme.com/room/openvas

# Task 1 - Intro
OpenVAS is an application used to scan endpoints and web apps to identify and detect vulnerabilities

* https://www.openvas.org/

# Task 2 - GVM Framework Architecture
OpenVAS is built off the GreenBone Vulernability Management (GVM) solution

* https://community.greenbone.net/t/about-gvm-10-architecture/1231

# Task 3 - Installing OpenVAS
Install options
1) repo
2) source
3) docker

After installation the console is available via localhost using admin/admin

```
sudo docker run -d -p 443:443 --name openvas mikesplain/openvas
Unable to find image 'mikesplain/openvas:latest' locally
latest: Pulling from mikesplain/openvas
34667c7e4631: Pull complete 
d18d76a881a4: Pull complete 
119c7358fbfc: Pull complete 
2aaf13f3eff0: Pull complete 
67b182362ac2: Pull complete 
c878d3d5e895: Pull complete 
ec12cc49fe18: Pull complete 
c4c454aeebef: Pull complete 
27d3410150b2: Pull complete 
e08d578dc278: Pull complete 
44951337cd32: Pull complete 
8c7fe885e62a: Pull complete 
a4f833680e45: Pull complete 
Digest: sha256:23c8412b5f9f370ba71e5cd3db36e6f2e269666cd8a3e3e7872f20f8063b2752
Status: Downloaded newer image for mikesplain/openvas:latest
debc7ee436bbd660d03706cbf600850dcb983f33196182d98fb2b956f079b2f0
```

# Task 4 - Initial Configuration
Scan yourself first to make sure the installation is working properly

# Task 5 - Scanning Infrastructure
Creating a task
* scans > tasks > click star > new task
* in new task screen give it a name
* in new task screen click star next to host, create a new host
* click create
Running a task
* click the play button

# Task 6 - Reporting and Continuous Monitoring
OpenVAS has a capable reporting and monitoring system, you can create schedules and alerts to report and notify you on items of interest

# Task 7 - Practical
Answer questions based on sample case file

# Task 8 - Conclusion
Docs
* https://docs.greenbone.net/