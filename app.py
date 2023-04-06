from flask import Flask, jsonify, request
from routes.user_route import user_bp
from routes.agricole_route import agricole_bp
from routes.otp import otp_bp
from db import mongo
import os


# settings app
app = Flask(__name__)
DEBUG = os.environ.get('DEBUG')
MONGO_URI = os.environ.get('MONGO_URI')
app.config['MONGO_URI'] = MONGO_URI
mongo.init_app(app)
app.secret_key = 'mysecretkey'

# blueprints
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(agricole_bp, url_prefix='/api')
app.register_blueprint(otp_bp, url_prefix='/api')




# Run Server
if __name__ == '__main__':
    app.run(debug=DEBUG)
