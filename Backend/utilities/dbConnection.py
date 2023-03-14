import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
from models.models import Base

load_dotenv()

def connect_to_db():
    user = os.environ.get('user')
    password = os.environ.get('password')
    host = os.environ.get('host')
    port = os.environ.get('port')
    database = os.environ.get('database')
    
    try:
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')    
        Session = sessionmaker(bind=engine)
        session = Session()

        # Creating an inspector to check for existing tables
        inspector = inspect(engine)
        existing_tables = inspector.get_table_names()
        
        # Create tables if they don't exist
        for table_name in Base.metadata.tables.keys():
            if table_name not in existing_tables:
                Base.metadata.tables[table_name].create(bind=engine)

        return engine, session

    except Exception as e:
        print(f"Error connecting to Database: {e}")
        return None, None