from flask import Flask


app = Flask(__name__)


@app.route('/')
def welcome_message():

    return 'Welcome to Redis and Flask App!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5002)