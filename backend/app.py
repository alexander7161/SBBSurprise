from flask import Flask, request
import surprise
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/categories')
def categories():
    return ['mountain']


@app.route('/surprise', methods=['POST'])
def surprisePost():
    return surprise.main()
