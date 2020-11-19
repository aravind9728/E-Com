from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Shop.db'

app.config['SECRET_KEY'] = 'sjhndi1JDOJSOa2pko3sak'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from shop.admin import routes


