from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, Flask!'


if __name__ == '__main__':
    # Debug mode is enabled for development only. Do not use in production.
    app.run(debug=True)
