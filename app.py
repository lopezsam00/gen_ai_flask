import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, Flask!'


if __name__ == '__main__':
    # Use environment variable to control debug mode (defaults to False for safety)
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)
