#!/usr/bin/env python3
"""
A basic Flask application with Jinja templates.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Route for the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Route for the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Route for the contact page."""
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
