# Room
https://tryhackme.com/room/torforbeginners

# Task 1 - Intro
Tor is free and open-source software that enables anonymous communication.  Internet traffic is directed through a free worldwide volunteer overlay network that conceals a user's location and usage

* Installation
  * apt-get install tor
  * service tor start
  * service tor status
  * service tor stop

# Task 2 - Proxychains
Proxychains is a tool that can force a TCP connection to use a proxy

* Resources
  * https://github.com/haad/proxychains

* Installation
  * apt install proxychains
  * vi /etc/proxychains.conf
    * uncomment dynamic_chain and proxy_dns
    * comment others
  * proxychains firefox

# Task 3 Tor Browser
Tor Browser transfers all its traffic through Tor

* Installation
  * apt-get install torbrowser-launcher