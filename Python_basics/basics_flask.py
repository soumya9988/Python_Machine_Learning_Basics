#!/usr/bin/python

# Import the flask module
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'


# Main module
if __name__ == '__main__':
    # start the app on local host.
    app.run(host='127.0.0.1', port=5000)