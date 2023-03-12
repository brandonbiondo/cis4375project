from dotenv import load_dotenv
from flask import Flask
from utilities.dbConnection import engine
from models.models import Base

load_dotenv()

app = Flask(__name__)


@app.route('/')
def hello():
    return f"Hello World"

if __name__ == '__main__':
    app.run()