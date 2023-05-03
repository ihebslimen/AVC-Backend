from flask import Flask, jsonify, request
from blueprints.admin import admin_bp
from blueprints.shared import shared_bp
from blueprints.user import user_bp
from routes.agricole_route import *
from routes.otp import *
from routes.user_route import * 
from routes.offer_route  import * 
from db import mongo
from models.actor import Actor
import os
from flask_cors import CORS

# settings app
app = Flask(__name__)
CORS(admin_bp)
CORS(shared_bp)
CORS(user_bp)
DEBUG = os.environ.get('DEBUG')
MONGO_URI = os.environ.get('MONGO_URI')
app.config['MONGO_URI'] = MONGO_URI
mongo.init_app(app)
app.secret_key = 'mysecretkey'
app.config['JWT_SECRET_KEY'] = 'mysecretkey'
# blueprints

app.register_blueprint(admin_bp, url_prefix='/api/admin')
app.register_blueprint(user_bp, url_prefix='/api/user')
app.register_blueprint(shared_bp, url_prefix='/api/shared')

@app.route('/hello', methods=['GET'])
def hello():
    return 'hello world'

""" # tester les instances
my_actor = Actor("actor")

@app.route('/public-key')
def get_public_key():
    return my_actor.getPubKey()

 """

CORS(app)

# Run Server
if __name__ == '__main__':
    app.run(debug=DEBUG)
