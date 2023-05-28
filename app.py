from flask import Flask, jsonify, request
from blueprints.admin import admin_bp
from blueprints.shared import shared_bp
from blueprints.user import user_bp
from routes.agricole_route import *
from routes.transformer_route import *
from routes.exporter_route import *
from routes.otp_route import *
from routes.user_route import * 
from routes.offer_route import * 
from routes.transaction_route import *
from routes.smart_contracts_route import *

from db import mongo
from models.actor import Actor
import os
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import config_web3


# settings app
app = Flask(__name__)
CORS_ALLOW_ORIGIN="*,*"
CORS_EXPOSE_HEADERS="*,*"
CORS_ALLOW_HEADERS="content-type,*"
CORS(admin_bp, origins='*', allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],   supports_credentials = True)
CORS(user_bp, origins='*', allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],   supports_credentials = True)
CORS(shared_bp, origins='*', allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],   supports_credentials = True)
CORS(app, origins='*', allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],   supports_credentials = True)
DEBUG = os.environ.get('DEBUG')
MONGO_URI = os.environ.get('MONGO_URI')
app.config['MONGO_URI'] = MONGO_URI
mongo.init_app(app)
app.secret_key = 'mysecretkey'

#### JWT Configuration
app.config['JWT_SECRET_KEY'] = 'mysecretkey'
app.config['JWT_TOKEN_LOCATION'] = "headers"
app.config['JWT_HEADER_NAME'] = "Authorization"
app.config["JWT_HEADER_TYPE"] = "Bearer"
app.config["JWT_IDENTITY_CLAIM"] = "user_id" # user_id is defined by mongodb


jwt = JWTManager(app)

# blueprints

app.register_blueprint(admin_bp, url_prefix='/api/admin')
app.register_blueprint(user_bp, url_prefix='/api/user')
app.register_blueprint(shared_bp, url_prefix='/api/shared')

CORS(app, origins='*', allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],   supports_credentials = True)



@app.before_request
def handle_preflight():
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE')
        return response


# Run Server
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=DEBUG)
