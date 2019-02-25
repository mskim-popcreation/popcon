from runserver import app
from models import Example, Image
from forms import LoginForm
from flask import render_template

@app.route('/')
def index():
    first_thing = Example.query.first()
    return '<h1>You are on the index! : ' + first_thing.data +'</h1>'

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('index.html', form=form)

@app.route('/image')
def image():
    images_first = Image.query.first()
    return "images_firsts : " + images_first.filename

