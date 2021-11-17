from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SECRET_KEY'] = '76ac3c1b34e08a2ac5851d7fa02bb689'

db = SQLAlchemy(app)
from nuturelab import routes