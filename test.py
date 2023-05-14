from flask import Flask, jsonify, request, Blueprint, routes

import os



app = Flask(__name__)
admin_bp = Blueprint('admin', __name__)


get = route('/', methods=['GET'])
def hello():
    return 'hello'

admin_bp.routes(get)

app.register_blueprint(admin_bp, url_prefix='/api/admin')


# Run Server
if __name__ == '__main__':
    app.run(debug=DEBUG)
