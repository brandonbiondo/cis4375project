from dotenv import load_dotenv
load_dotenv()
import mysql.connector
from mysql.connector import errorcode
from flask import Flask
import os
from utilities.dbConnection import connect_to_db
db = connect_to_db()

app = Flask(__name__)

@app.route('/')
def hello():
    return f"mysql+pymysql://{os.environ.get('user')}:{os.environ.get('password')}@{os.environ.get('host')}:{os.environ.get('port')}/{os.environ.get('database')}"

if __name__ == '__main__':
    app.run()