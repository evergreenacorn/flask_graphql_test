from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

app = Flask(__name__)
"""
<!-- md -->
## [Справка по конфигам](https://flask-sqlalchemy-russian.readthedocs.io/ru/latest/config.html)
<!-- end-md -->
"""
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'Hello!'
