# Room
https://tryhackme.com/room/phishingemails1tryoe

# Task 1 - Intro
* Common social engineering attacks
    * spam
    * phishing

# Task 2 - The email address
* Dates back to the 1970s from ARPANET
* name@domain.com
    * name : user mailbox
    * @
    * domain.com : domain name

# Task 3 - Email Delivery
* SMTP - simple mail transfer protocol - send mail
    * insecure : 25
    * secure : 465
* POP3 - post office protocol - transfer mail between client and server
    * insecure : 110
    * secure : 995
* IMAP - internet message access protocol - transfer mail between client and server
    * insecure : 143
    * secure : 993

# Task 4 - Email Headers
* Parts of an email
    * header
    * body
* A few email headers
    * from : sender email address
    * subject : email subject
    * date : date when email was sent
    * to : recipient email address

# Task 5 - Email Body
* Parse through the example exported emails to answer the challenge questions
* For question two copy the base64 encoded text to CyberChef, decode, save as PDF, grab the flag

# Task 6 - Types of Phishing
* Types of phishing
    * spam - unsolicited junk email sent to a large group of people
    * phishing - emails sent to a group of people to grab sensitive information
    * spear phishing - emails sent to a specific person or small group of people to grab sensitive information
    * whaling - emails sent to high value targets like CEOs, etc, to grab sensitive information
    * smishing - phishing on mobile devices via text messages
    * vishing - phishing through voice calls
* Defang URLs
    * https://www.ibm.com/docs/en/rsoa-and-rp/32.0?topic=SSBRUQ_32.0.0/com.ibm.resilient.doc/install/resilient_install_defangURLs.htm
* Review the saved email to answer the challenge questions.  CyberChef is a big help here.  Quoted printable helps, as does loading a file directly into CyberChef and using the built-in defang too.

# Task 7 - Conclusion
* BEC = Business Email Compromise
* Conclusion