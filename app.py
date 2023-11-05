"""
Simple Flask App
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Home Page"""
    return {"name": "Flask App"}, 200

@app.route('/health', methods=['GET'])
def health():
    """Health Check"""
    return {"status": "OK"}, 200

@app.route('/hello', methods=['GET'])
def hello():
    """Send back Hello world"""
    return {"message": "Hello World"}, 200

