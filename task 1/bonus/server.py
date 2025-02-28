from flask import Flask, request, jsonify, render_template, send_from_directory
import itertools
import string
import os

app = Flask(__name__)

PASSWORD = "Abcde"  

def dictionary_attack():
    try:
        with open("file.txt", "r") as file:
            for line in file:
                if line.strip() == PASSWORD:
                    return line.strip()
    except FileNotFoundError:
        return None
    return None

def brute_force_attack():
    for attempt in itertools.product(string.ascii_letters, repeat=5):
        guess = "".join(attempt)
        if guess == PASSWORD:
            return guess
    return None

@app.route('/')
def home():
    return send_from_directory(os.getcwd(), "index.html")  # Serve HTML file

@app.route('/crack', methods=['POST'])
def crack_password():
    if dictionary_attack():
        return jsonify({"method": "Dictionary Attack", "password": PASSWORD})

    return jsonify({"method": "Brute Force Attack", "password": brute_force_attack()})

if __name__ == "__main__":
    app.run(debug=True)
