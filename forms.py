# from flask.ext.wtf import Form
from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField

class LoginForm(FlaskForm):
    username = TextField('username')
    password = PasswordField('password')
