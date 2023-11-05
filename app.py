"""
Simple Flask App
"""
import os

PORT = int(os.getenv('PORT', '8080'))

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)

