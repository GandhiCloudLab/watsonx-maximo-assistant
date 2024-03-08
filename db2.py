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
# import ibm_db

from maximo import MaximoHandler
from flask_restx import Api, Resource, fields


class DB2Handler(object):


    # API endpoint to get all books
    def get(self):
        ENV_DB_DATABASE = os.environ.get('DB_DATABASE')
        ENV_DB_HOSTNAME = os.environ.get('DB_HOSTNAME')
        ENV_DB_PORT = os.environ.get('DB_PORT')
        ENV_DB_USER = os.environ.get('DB_USER')
        ENV_DB_PASSWORD = os.environ.get('DB_PASSWORD')

        # # Define And Initialize The Appropriate Variables
        # dbName = ENV_DB_DATABASE        # The Alias For The Cataloged, Local Database
        # userID = ENV_DB_USER    # The Instance User ID At The Local Server
        # passWord = ENV_DB_PASSWORD    # The Password For The Instance User ID At The Local Server
        # connOption = {ibm_db.SQL_ATTR_AUTOCOMMIT: ibm_db.SQL_AUTOCOMMIT_ON}
        # connectionID = None
        # resultSet = False

        # # Display A Status Message Indicating An Attempt To Establish A Connection To A Db2 Database
        # # Is About To Be Made
        # print("\nConnecting to the \'" + dbName + "\' database ... ", end="")

        # # Construct The String That Will Be Used To Establish A Db2 Database Connection
        # connString = "ATTACH=FALSE"              # Attach To A Database; Not A Server
        # connString += ";DATABASE=" + dbName      # Required To Connect To A Database     
        # connString += ";PROTOCOL=TCPIP"
        # connString += ";UID=" + userID
        # connString += ";PWD=" + passWord
        # connString += ";HOSTNAME=" + ENV_DB_HOSTNAME
        # connString += ";PORT=" + ENV_DB_PORT

        # # Attempt To Establish A Connection To The Database Specified
        # try:
        #     connectionID = ibm_db.connect(connString, '', '', connOption, 
        #         ibm_db.QUOTED_LITERAL_REPLACEMENT_OFF)
        # except Exception:
        #     pass

        # # If A Db2 Database Connection Could Not Be Established, Display An Error Message And Exit
        # if connectionID is None:
        #     print("\nERROR: Unable to connect to the \'" + dbName + "\' database.")
        #     print("Connection string used: " + connString + "\n")
        #     exit(-1)

        # # Otherwise, Complete The Status Message
        # else:
        #     print("Done!\n")
            
        # # Define The SQL Statement That Is To Be Executed
        # sqlStatement = "SELECT deptname FROM org WHERE deptnumb = '50000'"

        # # Execute The SQL Statement Just Defined
        # print("Executing the SQL statement \"" + sqlStatement + "\" ... ", end="")
        # try:
        #     resultSet = ibm_db.exec_immediate(connectionID, sqlStatement)
        # except Exception:
        #     pass

        # # If The SQL Statement Could Not Be Executed, Display An Error Message And Exit 
        # if resultSet is False:
        #     print("\nERROR: Unable to execute the SQL statement specified.\n")
        #     if not connectionID is None:
        #         ibm_db.close(connectionID)
        #     exit(-1)

        # # Otherwise, Complete The Status Message
        # else:
        #     print("Done!\n") 
            
        # # Attempt To Close The Db2 Database Connection That Was Opened Earlier
        # if not connectionID is None:
        #     print("Disconnecting from the \'" + dbName + "\' database ... ", end="")
        #     try:
        #         returnCode = ibm_db.close(connectionID)
        #     except Exception:
        #         pass

        #     # If The Db2 Database Connection Was Not Closed, Display An Error Message And Exit
        #     if returnCode is False:
        #         print("\nERROR: Unable to disconnect from the " + dbName + " database.")
        #         exit(-1)

        #     # Otherwise, Complete The Status Message
        #     else:
        #         print("Done!\n")

        # Return Control To The Operating System
        exit()