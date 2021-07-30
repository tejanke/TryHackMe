# Room
https://tryhackme.com/room/flask

# Task 1 - Intro
Flask is a micro web framework written in Python

* Room examples
  * https://github.com/Swafox/Flask-examples

# Task 2 - Installation
* Installation
  * pip3 install Flask
  * pip3 install virtualenv

* Create example project
  * mkdir project
  * cd project
  * python3 -m venv venv
  * export FLASK_APP=test.py
  * flask run
  * flask run --host=0.0.0.0

# Task 3 - Syntax and Routing
Basic Hello World
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/admin')
def admin():
    return 'Admin page'
```

* By default Flask uses TCP port 5000

# Task 4 - HTTP Methods
* HTTP Methods
  * GET
  * POST
* By default a route only answers GET requests
* Flask supports using HTML for making templates

# Task 5 - Files
* File functions
  * files
  * save()

# Task 6 - Flask Injection
* One prior vulnerability was in Flask's template rendering engine

# Task 7 - Conclusion
Conclusion