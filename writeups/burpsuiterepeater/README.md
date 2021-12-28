# Room
https://tryhackme.com/room/burpsuiterepeater

# Task 1 - Intro
Intro

# Task 2 - What is repeater?
* Repeater allows you to craft and relay or intercept requests to a target

# Task 3 - Basic usage
* More useful to capture an example request and manipulate it from there then to craft it yourself manually

# Task 4 - Views
* Change the way the response is viewed
    * Pretty - beautify response
    * Raw
    * Hex
    * Render
    * \n - show non-printable characters

# Task 5 - Inspector
* Right hand side of the window that gives a list of the components in the request and response
* You can modify requests directly from the Inspector view

# Task 6 - Example
* Open the web browser and enable Burp in FoxyProxy.  Open Burp and turn off intercept.  Navigate to the challenge VM website to capture a request passively in Burp.  Go to Burp proxy history and send the request to repeater.  In the repeater window send the request once to verify it works.  Next, add an HTTP header to grab the challenge flag.

# Task 7 - Challenge
* Open the web browser and enable Burp in FoxyProxy.  Open Burp and turn off intercept.  Navigate to the challenge VM website to capture a request passively in Burp from the products page.  Go to Burp proxy history and send the request to repeater.  In the repeater window send the request once to verify it works.  Next, modify the URI input to an inappropriate value to grab the flag.

# Task 8 - SQLi with Repeater
* Open the web browser and enable Burp in FoxyProxy.  Open Burp and turn off intercept.  Navigate to the challenge VM website to capture a request passively in Burp from the about page.  Go to Burp proxy history and send the request to repeater.  In the repeater window send the request once to verify it works.  Next, modify the GET request to step through a SQLi and find the flag.

# Task 9 - Conclusion
Conclusion