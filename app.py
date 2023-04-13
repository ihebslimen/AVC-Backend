from flask import Flask, jsonify, request
from blueprints.admin import admin_bp
from blueprints.shared import shared_bp
from blueprints.user import user_bp
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_security import Security
from routes.agricole_route import *
from routes.otp import *
from routes.user_route import * 
from db import mongo
import os

# settings app
app = Flask(__name__)
DEBUG = os.environ.get('DEBUG')
MONGO_URI = os.environ.get('MONGO_URI')
app.config['MONGO_URI'] = MONGO_URI
mongo.init_app(app)
app.secret_key = 'mysecretkey'
app.config['JWT_SECRET_KEY'] = 'mysecretkey'
jwt = JWTManager(app)
# blueprints

app.register_blueprint(admin_bp, url_prefix='/api/admin')
app.register_blueprint(user_bp, url_prefix='/api/admin')
app.register_blueprint(shared_bp, url_prefix='/api/shared')





# Run Server
if __name__ == '__main__':
    app.run(debug=DEBUG)
