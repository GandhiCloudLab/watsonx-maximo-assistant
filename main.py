from flask import Flask, jsonify, request
from flask_cors import CORS

import os
import argparse
import logging 
import socket
import sys
import json
import os, pandas as pd
# import ibm_db
import requests
from dotenv import load_dotenv
import os, json

from flask_restx import Api, Resource, fields

app = Flask(__name__, static_folder='./static', static_url_path='/')
CORS(app)

# Initialize Flask-RestX API with OpenAPI version
api = Api(app, version='1.0', title='Sample API', description='A simple sample API', 
          doc='/swagger',  # Route for accessing the Swagger UI
          openapi_version='3.0.2'  # Specify the OpenAPI version here
)

# Sample data
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"}
]

# Define a simple homepage route
@app.route('/')
def home():
    return app.send_static_file('index.html')

ns = api.namespace('hello', description='Hello API')
@ns.route('/')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    
    def getAll(self):
        return {'hello1': 'world1'}
    
ns = api.namespace('books', description='Books operations')
@ns.route('/')
class Books(Resource):
    # API endpoint to get all books
    def get(self):
        return jsonify(books)

    # API endpoint to get a specific book by its ID
    def get_book(self, id):
        book = next((book for book in books if book['id'] == id), None)
        if book:
            return jsonify(book)
        return jsonify({"message": "Book not found"}), 404

@ns.route('/<int:id>')
@ns.param('id', 'The books identifier')
class Books2(Resource):
    @ns.doc('get_book')
    def get(self, id):
        book = next((book for book in books if book['id'] == id), None)
        if book:
            return jsonify(book)
        return jsonify({"message": "Book not found"}), 404

def main():
  logging.info("main started .....")

if __name__ == '__main__':
  main()
  app.run(host ='0.0.0.0', port = 8080, debug = True)