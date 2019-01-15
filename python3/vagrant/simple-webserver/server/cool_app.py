#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'I AM VAGRANT HAHA!!!'


if __name__ == '__main__':
    
    # This allows us to bind to all interfaces and let everyone see us (everyone being vagrant)
    app.run("0.0.0.0", debug=True)
