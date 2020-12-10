from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1234@34.105.208.208/todolsit"
app.config["SECRET_KEY"] = "SDRFHESDRTHSDFTGB"

db = SQLAlchemy(app)

from application import routes 