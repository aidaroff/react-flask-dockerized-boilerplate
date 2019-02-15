import os

from flask import Flask


app = Flask(__name__)
app.config.from_object(os.environ.get('CONFIG', 'app.config.DevelopmentConfig'))

@app.route('/')
def hello_world():
    return 'You\'re running the Flask app'

@app.errorhandler(404)
def page_not_found(e):
    return 'Invalid url'
