from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.debug = True
app.config.from_pyfile('config.py')
# app.config['DEBUG'] = True
db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug = True)