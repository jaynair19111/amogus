from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///noodle.db'
app.config["SECRET_KEY"] = "among us"
app.config['UPLOAD_FOLDER'] = 'static/images'
db = SQLAlchemy(app)

from app import routes,models,forms
