from flask import Flask
from flask_redis import FlaskRedis


app = Flask(__name__)


app.config['REDIS_URL'] = 'redis://redis:6379/0'

redis_client = FlaskRedis(app)


@app.route('/')
def welcome_message():

    return 'Welcome to Redis and Flask App!'

@app.route('/count')
def count():
    redis_client.incr('hits')
    count = redis_client.get('hits')

    return f'This page has been visited {count.decode()} times'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5002)