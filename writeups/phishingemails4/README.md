# room
https://tryhackme.com/room/phishingemails4gkxh

# task 1 - intro
* some protections against phishing
    * spf, dkim, dmarc
    * spam filters
    * email labels
    * email address / domain / url blocking
    * attachment blocking
    * attachment sandboxing
    * security awareness training

# task 2 - spf - sender policy framework
* spf - sender policy framework
* spf is used to authenticate the sender of an email
* spf allows ISPs to verify that a mail server is authorized to send email for a specific domain
* spf records are dns txt records containing a list of ip addresses that are allowed to send email on behalf of a domain
* spf record example
    * v=spf1 ipv4:127.0.0.1 include:_spf.google.com -all
        * v=spf1 - start of spf record
        * ipv4:127.0.0.1 - which ip can send mail
        * include:_spf.google.com - which domain can send mail
        * -all - non authorized emails will be rejected
* resources
    * https://dmarcian.com/spf-survey/

# task 3 - dkim - domainkeys identified mail
* dkim - domainkeys identified mail
* dkim is used for authentication of an email that is being sent
* dkim records exist in dns
* dkim can survive forwarding where spf cannot
* dkim record example
    * v=dkim1; k=rsa; p=[rsa public key]
        * v=dkim1 - version of dkim record, optional
        * k=rsa - key type, algorithm used
        * p= - public key
* resources
    * https://dmarcian.com/dkim-selectors/

# task 4 - dmarc - domain based message authentication, reporting, and conformance
* dmarc - domain based message authentication, reporting, and conformance
* dmarc uses a concept called alignment to tie the result of spf and dkim to the content of ane mail
* dmarc allows you to troubleshoot spf and dkim configurations
* dmarc example
    * v=dmarc1; p=quarantine; rua=mailto:post@example.com
        * v=DMARC1 - must be in ALL CAPS, not optional
        * p=quarantine - if check fails, sent to spam folder
        * rua=mailto:post@example.com - reports sent to this address
* resources
    * https://dmarcian.com/dmarc-record/
    * https://dmarcian.com/domain-checker/

# task 5 - s/mime - secure / multipurpose internet mail extensions
* s/mime - secure / multipurpose internet mail extensions
* s/mime is a protocol for sending digitally signed and encrypted messages
* s/mime components
    * digital signatures
    * encryption
* s/mime uses pki
* resources
    * https://docs.microsoft.com/en-us/exchange/security-and-compliance/smime-exo/smime-exo

# task 6 - smtp status codes - practical
* analyze the pcap
    * use the wireshark filter resource kit
    * smtp.response contains "spam"
* resources
    * https://www.wireshark.org/docs/dfref/s/smtp.html
    * https://www.mailersend.com/blog/smtp-codes

# task 7 - smtp traffic analysis - practical
* analyze the pcap
    * use the wireshark filter resource kit
    * frame contains 43:6f:6e:74:65:6e:74:2d:44:69:73:70:6f:73:69:74:69:6f:6e:3a:20:61:74:74:61:63:68:6d:65:6e:74:3b:0d:0a
        * this is the frame contents for "Content-Disposition: attachment;\r\n"

# task 8 - smtp and c&c communication
* resources
    * https://attack.mitre.org/techniques/T1071/003/

# task 9 - conclusion
* resources
    * https://www.incidentresponse.com/playbooks/phishing
    * https://www.malware-traffic-analysis.net/2018/12/19/index.html