# Room
https://tryhackme.com/room/wifihacking101

# Task 1 - Basics
* SSID - network name
* ESSID - SSID that may apply to multiple APs
* BSSID - AP MAC address
* WPA2-PSK - WPA2 enabled with a password
* WPA2-EAP - WPA2 enabled with RADIUS authentication
* RADIUS - a server authentication mechanism

* WPA2
  * 4 way handshake
    * proves client and AP know the key without telling each other
  * keys derived from ESSID and password
    * ESSID is a salt

# Task 2 - Packet captures
* Aircrack-ng
  * https://www.aircrack-ng.org/

* Some useful tools in the suite
  * aircrack-ng
  * airmon-ng
  * airodump-ng

# Task 3 - Packet capture review
* Download the example capture
* Use aircrack-ng to extract a hash for cracking
  * aircrack-ng NinjaJc01-01.cap -j hash
* Use hashcat to crack the hash with rockyou.txt
  * .\hashcat.exe -m 2500 .\hash.hccapx .\rockyou.txt