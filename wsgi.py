"""
WSGI application
"""
import os
from app import app

PORT = int(os.getenv('PORT', '8080'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)

