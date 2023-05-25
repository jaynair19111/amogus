from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///noodle.db'
app.config["SECRET_KEY"] = "among us"
db = SQLAlchemy(app)

from app import routes,models,forms
#program
