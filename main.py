from flask import Flask, jsonify, request
from flask_cors import CORS

import os
import argparse
import logging 
import socket

app = Flask(__name__, static_folder='./static', static_url_path='/')
CORS(app)

# Sample data
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"}
]

@app.route('/')
def index():
    return app.send_static_file('index.html')

# API endpoint to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# API endpoint to get a specific book by its ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

def main():
  logging.info("main started .....")

if __name__ == '__main__':
  main()
  app.run(host ='0.0.0.0', port = 8080, debug = True)