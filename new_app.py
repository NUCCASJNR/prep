#!/usr/bin/python3
from os import getenv
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html')

@app.route('/post', strict_slashes=False)
def post():
    return render_template('post.html')

@app.route('/about', strict_slashes=False)
def about():
    return render_template('about.html')
@app.route('/contact', strict_slashes=False)
def contact():
    return render_template('contact.html')
if __name__ == "__main__":
    host = getenv("HBNB_API_HOST")
    port = getenv("HBNB_API_PORT")
    app.run(host=host, port=port, debug=True)
