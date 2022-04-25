from flask import Flask, request, jsonify
from flask_restful import Rescource, Api


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_stocks():
    input = request.args.get('input')
    result = main(input)
    return jsonify(result)
