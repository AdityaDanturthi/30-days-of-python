# Panadas for web

# Creating routes

# Home route
from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def home ():
    return '<h1>Hi</h1>'

@app.route('/about')
def about ():
    return '<h1>About me</h1>'

if __name__ == '__main__':
    port = int(os.environ.get("Port", 5000))
    app.run(debug = True, host = '0.0.0.0', port = port)

