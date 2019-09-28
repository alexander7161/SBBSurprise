from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import surprise
app = Flask(__name__)
CORS(app)
port = int(os.getenv("PORT", 8080))

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/categories')
def categories():
    categories = ['mountain','castle','swim','place','shopping_mall','amusement_park','art_gallery','museum']
    return jsonify(categories)



@app.route('/surprise', methods=['POST'])
def surprisePost():
    return surprise.main()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)