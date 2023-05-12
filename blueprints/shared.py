
from flask import Blueprint, jsonify, request
from flask_cors import CORS

shared_bp = Blueprint('shared', __name__)
CORS(shared_bp)
