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