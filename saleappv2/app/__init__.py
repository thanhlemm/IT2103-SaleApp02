from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy

#hi
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/flashsaledb?charset=utf8mb4" % quote('t-TThanhlemmilkk021203')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app = app)