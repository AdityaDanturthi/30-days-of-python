# Python for web

# Creating routes

# Home route
from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)

@app.route('/')
def home():
    tech = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days of Python'
    return render_template('home.html', tech = tech, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '30 Days of Python'
    return render_template('about.html', name = name, title = 'About Me')

@app.route('/post')
def post():
    name = 'Text Analyzer'
    return render_template('post.html', name = name, title = name)

if __name__ == '__main__':
    port = int(os.environ.get("Port", 5000))
    app.run(debug = True, host = '0.0.0.0', port = port)