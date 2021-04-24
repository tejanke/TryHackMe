# Room
https://tryhackme.com/room/osqueryf8

# Task 1 - Intro
Osquery is an open source tool created by Facebook
* https://osquery.io/

Osquery allows you to query an endpoint using SQL syntax.  Some open source and commercial tools utilize Osquery including Alienvault and Cisco

# Task 2 - Installation
Install docs by OS
* Windows
  * https://osquery.readthedocs.io/en/stable/installation/install-windows/
* Linux
  * https://osquery.readthedocs.io/en/stable/installation/install-linux/
* macOS
  * https://osquery.readthedocs.io/en/stable/installation/install-macos/
* FreeBSD
  * https://osquery.readthedocs.io/en/stable/installation/install-freebsd/

Useful CLI flags
* https://osquery.readthedocs.io/en/latest/installation/cli-flags/

Example Linux Install
```
wget https://pkg.osquery.io/deb/osquery_4.8.0-1.linux_amd64.deb                                            [195/247]
--2021-04-21 10:45:32--  https://pkg.osquery.io/deb/osquery_4.8.0-1.linux_amd64.deb                                                                           
Resolving pkg.osquery.io (pkg.osquery.io)... 199.232.10.133                                                                                                   
Connecting to pkg.osquery.io (pkg.osquery.io)|199.232.10.133|:443... connected.                                                                               
HTTP request sent, awaiting response... 200 OK                                                                                                                
Length: 16376890 (16M) [application/vnd.debian.binary-package]                                                                                                
Saving to: ‘osquery_4.8.0-1.linux_amd64.deb’                                                                                                                  
osquery_4.8.0-1.linux_amd64.deb         100%[=============================================================================>]  15.62M  2.82MB/s    in 5.5s     
2021-04-21 10:45:38 (2.82 MB/s) - ‘osquery_4.8.0-1.linux_amd64.deb’ saved [16376890/16376890]                                                                 
                                                                                                                                                              

sudo dpkg -i osquery_4.8.0-1.linux_amd64.deb                                                                        
Selecting previously unselected package osquery.                                                                                                              
(Reading database ... 506787 files and directories currently installed.)                                                                                      
Preparing to unpack osquery_4.8.0-1.linux_amd64.deb ...                                                                                                       
Unpacking osquery (4.8.0-1.linux) ...                                                                                                                         
Setting up osquery (4.8.0-1.linux) ...                                                                                                                        
1274                                                                                                                                                          
Processing triggers for kali-menu (2021.2.0) ...                                                                                                              


osqueryi --help                                                                                                     
osquery 4.8.0, your OS as a high-performance relational database                                                                                              
Usage: osqueryi [OPTION]... [SQL STATEMENT]                                                                      
```

# Task 3 - Osquery Shell
* osqueryi is a modified version of the SQLite shell
```
osqueryi
Using a virtual database. Need help, type '.help'
osquery> 
```
* help
```
osquery> .help
Welcome to the osquery shell. Please explore your OS!
You are connected to a transient 'in-memory' virtual database.

.all [TABLE]     Select all from a table
```
* list tables
```
osquery> .tables 
```
* list tables that relate to processes
```
osquery> .tables process
  => process_envs
```
* list schema for the processes table
```
osquery> .schema processes
CREATE TABLE processes(`pid` BIGINT, `name` TEXT, `path` TEXT, `cmdline` TEXT, `state` TEXT, `cwd` TEXT, `root` TEXT, `uid` BIGINT, `gid` BIGINT, `euid` BIGINT, `egid` BIGINT, `suid` BIGINT, `sgid` BIGINT, `on_disk` INTEGER, `wired_size` BIGINT, `resident_size` BIGINT, `total_size` BIGINT, `user_time` BIGINT, `system_time` BIGINT, `disk_bytes_read` BIGINT, `disk_bytes_written` BIGINT, `start_time` BIGINT, `parent` BIGINT, `pgroup` BIGINT, `threads` INTEGER, `nice` INTEGER, `is_elevated_token` INTEGER HIDDEN, `elapsed_time` BIGINT HIDDEN, `handle_count` BIGINT HIDDEN, `percent_processor_time` BIGINT HIDDEN, `upid` BIGINT HIDDEN, `uppid` BIGINT HIDDEN, `cpu_type` INTEGER HIDDEN, `cpu_subtype` INTEGER HIDDEN, `phys_footprint` BIGINT HIDDEN, PRIMARY KEY (`pid`)) WITHOUT ROWID;
```
* show defaults
```
.show
```
* change output mode
```
.mode
```
* exit the application
```
.quit
```

# Task 4 - Schema Documentation
Schema documentation is listed here
* https://osquery.io/schema/4.7.0/

Answer questions based on the documentation link above

# Task 5 - Creating queries
SQL implemented in Osquery is not the entire language, but a subset

Example queries
* select pid, name, path from processes;
* select count(*) from processes;
* select pid, name, path from processes where name='lsass.exe';

Filtering operators
* = : equal
* <> : not equal
* > and >= : greater than and greater than or equal
* < and <= : less than and less than or equal
* BETWEEN : between a range
* LIKE : pattern wildcard search
* % : wildcard with multiple choices
* _ : wildcard with one character

Wildcard rules
* % : match all files and folders for one level
* %% : match all files and folders recursively
* %abc : match all ending with abc
* abc% : match all beginning with abc

Wildcard examples
* /users/%/library : monitor every user library folder
* /users/%/library/ : monitor changes within each library folder
* /users/%/library/% : same as above
* /users/%/library/%% : recursively
* /bin/%sh : monitor bin for changes ending in sh

# Task 6 - Kolide Fleet
Kolide Fleet is an Osquery fleet manager that allows you to query multiple endpoints instead of each individually

Commercial
* https://www.kolide.com/launcher/

Open source fork
* https://github.com/fleetdm/fleet

# Task 7 - Extensions
Extension links
* https://github.com/trailofbits/osquery-extensions
* https://github.com/polylogyx/osq-ext-bin

