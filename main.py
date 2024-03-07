from flask import Flask, jsonify, request
from flask_cors import CORS

import os
import argparse
import logging 
import socket
import sys
import json
import os, ibm_db, pandas as pd
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


# # API endpoint to get all books
# @app.route('/order', methods=['GET'])
# def get_order(params):

#     ENV_DB_DATABASE = os.environ.get('DB_DATABASE')
#     ENV_DB_HOSTNAME = os.environ.get('DB_HOSTNAME')
#     ENV_DB_PORT = os.environ.get('DB_PORT')
#     ENV_DB_USER = os.environ.get('DB_USER')
#     ENV_DB_PASSWORD = os.environ.get('DB_PASSWORD')

#     db2_dsn = 'DATABASE={};HOSTNAME={};PORT={};PROTOCOL=TCPIP;UID={uid};PWD={pwd};SECURITY=SSL'.format(
#         {ENV_DB_DATABASE},
#         {ENV_DB_HOSTNAME},
#         {ENV_DB_PORT},
#         uid={ENV_DB_USER},
#         pwd={ENV_DB_PASSWORD}
#     )

#     conn = dbi.connect(db2_dsn)
#     query = 'SELECT * FROM "Maximo"."WORKORDER"'
#     df = pd.read_sql_query(query, con=conn)
#     dbi.close(conn)

#     # Convert DataFrame to JSON and return as response
#     response = df.to_json(orient='records')

#     return response

# API endpoint to get all books
@app.route('/order2', methods=['GET'])
def get_order2(params):

    ENV_DB_DATABASE = os.environ.get('DB_DATABASE')
    ENV_DB_HOSTNAME = os.environ.get('DB_HOSTNAME')
    ENV_DB_PORT = os.environ.get('DB_PORT')
    ENV_DB_USER = os.environ.get('DB_USER')
    ENV_DB_PASSWORD = os.environ.get('DB_PASSWORD')


    # Define And Initialize The Appropriate Variables
    dbName = ENV_DB_DATABASE        # The Alias For The Cataloged, Local Database
    userID = ENV_DB_USER    # The Instance User ID At The Local Server
    passWord = ENV_DB_PASSWORD    # The Password For The Instance User ID At The Local Server
    connOption = {ibm_db.SQL_ATTR_AUTOCOMMIT: ibm_db.SQL_AUTOCOMMIT_ON}
    connectionID = None
    resultSet = False

    # Display A Status Message Indicating An Attempt To Establish A Connection To A Db2 Database
    # Is About To Be Made
    print("\nConnecting to the \'" + dbName + "\' database ... ", end="")

    # Construct The String That Will Be Used To Establish A Db2 Database Connection
    connString = "ATTACH=FALSE"              # Attach To A Database; Not A Server
    connString += ";DATABASE=" + dbName      # Required To Connect To A Database     
    connString += ";PROTOCOL=TCPIP"
    connString += ";UID=" + userID
    connString += ";PWD=" + passWord
    connString += ";HOSTNAME=" + ENV_DB_HOSTNAME
    connString += ";PORT=" + ENV_DB_PORT

    # Attempt To Establish A Connection To The Database Specified
    try:
        connectionID = ibm_db.connect(connString, '', '', connOption, 
            ibm_db.QUOTED_LITERAL_REPLACEMENT_OFF)
    except Exception:
        pass

    # If A Db2 Database Connection Could Not Be Established, Display An Error Message And Exit
    if connectionID is None:
        print("\nERROR: Unable to connect to the \'" + dbName + "\' database.")
        print("Connection string used: " + connString + "\n")
        exit(-1)

    # Otherwise, Complete The Status Message
    else:
        print("Done!\n")
        
    # Define The SQL Statement That Is To Be Executed
    sqlStatement = "SELECT deptname FROM org WHERE deptnumb = '50000'"

    # Execute The SQL Statement Just Defined
    print("Executing the SQL statement \"" + sqlStatement + "\" ... ", end="")
    try:
        resultSet = ibm_db.exec_immediate(connectionID, sqlStatement)
    except Exception:
        pass

    # If The SQL Statement Could Not Be Executed, Display An Error Message And Exit 
    if resultSet is False:
        print("\nERROR: Unable to execute the SQL statement specified.\n")
        if not connectionID is None:
            ibm_db.close(connectionID)
        exit(-1)

    # Otherwise, Complete The Status Message
    else:
        print("Done!\n") 
        
    # Attempt To Close The Db2 Database Connection That Was Opened Earlier
    if not connectionID is None:
        print("Disconnecting from the \'" + dbName + "\' database ... ", end="")
        try:
            returnCode = ibm_db.close(connectionID)
        except Exception:
            pass

        # If The Db2 Database Connection Was Not Closed, Display An Error Message And Exit
        if returnCode is False:
            print("\nERROR: Unable to disconnect from the " + dbName + " database.")
            exit(-1)

        # Otherwise, Complete The Status Message
        else:
            print("Done!\n")

    # Return Control To The Operating System
    exit()

def main():
  logging.info("main started .....")

if __name__ == '__main__':
  main()
  app.run(host ='0.0.0.0', port = 8080, debug = True)