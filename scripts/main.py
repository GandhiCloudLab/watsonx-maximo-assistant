from flask import Flask, jsonify, request
from flask_cors import CORS

import os
import argparse
import logging 
import socket
import sys
import json
import os, ibm_db, ibm_db_dbi as dbi, pandas as pd
import requests
from dotenv import load_dotenv
import os, json

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


# API endpoint to get all books
@app.route('/order', methods=['GET'])
def get_order(params):

    ENV_DB_DATABASE = os.environ.get('DB_DATABASE')
    ENV_DB_HOSTNAME = os.environ.get('DB_HOSTNAME')
    ENV_DB_PORT = os.environ.get('DB_PORT')
    ENV_DB_USER = os.environ.get('DB_USER')
    ENV_DB_PASSWORD = os.environ.get('DB_PASSWORD')

    db2_dsn = 'DATABASE={};HOSTNAME={};PORT={};PROTOCOL=TCPIP;UID={uid};PWD={pwd};SECURITY=SSL'.format(
        {ENV_DB_DATABASE},
        {ENV_DB_HOSTNAME},
        {ENV_DB_PORT},
        uid={ENV_DB_USER},
        pwd={ENV_DB_PASSWORD}
    )
    
    conn = dbi.connect(db2_dsn)
    query = 'SELECT * FROM "Maximo"."WORKORDER"'
    df = pd.read_sql_query(query, con=conn)
    dbi.close(conn)

    # Convert DataFrame to JSON and return as response
    response = df.to_json(orient='records')

    return response

def main():
  logging.info("main started .....")

if __name__ == '__main__':
  main()
  app.run(host ='0.0.0.0', port = 8080, debug = True)