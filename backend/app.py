from flask import Flask, request, Response, jsonify, json
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
    value = {
        "categories": ['mountain','castle','swim','place','shopping_mall','amusement_park','art_gallery','museum']
    }
    return Response(json.dumps(value), mimetype='application/json')



@app.route('/surprise', methods=['POST'])
def surprisePost():
    return surprise.main()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)