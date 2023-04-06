from flask import Flask
from flask_pymongo import PyMongo, ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

mongo = PyMongo()