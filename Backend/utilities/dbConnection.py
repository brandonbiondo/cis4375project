# Importing SQLAlchemy Engine
from sqlalchemy import create_engine
import os
import pymysql

# Python Function to connect to the DB
# Return SQLAlchemy Object
def connect_to_db():
	try:
		print(f"Connection to the {os.environ.get('host')} for user {os.environ.get('user')} created successfully.")	
		return create_engine(
			url=f"mysql+pymysql://{os.environ.get('user')}:{os.environ.get('password')}@{os.environ.get('host')}:{os.environ.get('port')}/{os.environ.get('database')}"
		)
	except Exception as ex:
		print("Connection could not be made due to the following error: \n", ex)