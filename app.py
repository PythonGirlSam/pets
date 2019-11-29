from flask import Flask
from flask_cors import CORS
from flask import Blueprint
from flask import jsonify

import time
# Configurations
DEBUG = True

# App instantiation
app = Flask(__name__)
CORS(app)

pets = Blueprint('pets', __name__, url_prefix='/v1')


@pets.route('/pets', methods=['GET'])
def fetch_data():
    data = {'pets':['dog','cat','rats','birds']}
    return jsonify(data), 200


@pets.route('/pets', methods=['POST'])
def create_pets():
    data = {'dog':'Oh yes!!'}
    return jsonify(data), 200

def create_app():
    app.register_blueprint(pets)
    return app

def run_app():
    app = create_app()
    app.run(
        host="0.0.0.0",
        port=9000,
        debug=DEBUG
    )

if __name__ == '__main__':
    run_app()
