#!/usr/bin/python3
"""Simple Flask API implementation"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route('/')
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Return list of usernames"""
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """Return API status"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Return user data for given username"""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add new user to the API"""
    data = request.get_json()

    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']
    users[username] = {
        "username": username,
        "name": data.get('name', ''),
        "age": data.get('age', 0),
        "city": data.get('city', '')
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == '__main__':
    app.run(debug=True)
