from flask import Flask, jsonify
from dotenv import load_dotenv
from crudops.restapi import bp

load_dotenv()

app = Flask(__name__)
app.config["DEBUG"] = True

app.register_blueprint(bp)

@app.route('/')
def default():
    return 'Hello World'

if __name__ == '__main__':
    app.run()
