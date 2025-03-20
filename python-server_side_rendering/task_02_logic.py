#!/usr/bin/env python3
"""
A Flask application demonstrating Jinja template logic with loops and conditionals.
"""
import json
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


@app.route('/items')
def items():
    """Route for the items page that demonstrates Jinja logic."""
    try:
        # Read items from the JSON file
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        # Handle errors by returning an empty list
        print(f"Error loading items: {e}")
        items_list = []
    
    # Render the template with the items
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
