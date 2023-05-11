from app import app,db
from app.models import Noodle
from app.forms import MyForm,ItemEntry
from flask import render_template

@app.route('/',methods=["GET", "POST"])
def home():
    items = Noodle.query.all()
    print(items)
    return render_template("index.html",items=items)

@app.route('/',methods=["GET", "POST"])
def login():
    print("login man")
    