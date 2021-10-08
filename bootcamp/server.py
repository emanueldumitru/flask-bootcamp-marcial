from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, BooleanField, DateTimeField, 
                     RadioField, SelectField, TextField,
                     TextAreaField, SubmitField)
from flask import flash

from wtforms.validators import DataRequired
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname((__file__)))
print(basedir)


# pip freeze > requirements.txt
# export FLASK_APP=server.py


""" 
Flask migrations

flask db init

flask db migrate -m "migration 1"

flask db upgrade

"""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

#######################################################

class Puppy(db.Model):
    __tablename__ = 'puppies'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)
    # ONE TO MANY 
    # PUPPY TO MANY TOYS
    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')
    
    #ONE TO ONE
    owner = db.relationship('Owner', backref='puppy', uselist=False)
    
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def __repr__(self):
        if self.owner:
            return f"Puppy {self.name} is {self.age} year/s old with {self.breed}. Owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and has no owner yet!"
        
    def report_toys(self):
        print("Here are my toys: ")
        for toy in self.toys:
            print(toy.item_name)
    

class Toy(db.Model):
    __tablename__ = 'toys'
    
    id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))
    
    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id
    

class Owner(db.Model):
    __tablename__ = 'owners'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))
    
    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id
        
    

#######################################################

@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'

@app.route('/venus')
def venus():
    some_variable = "Fuck you"
    my_fucking_list = ['Fuck', 'you', 'man']
    return render_template('index.html', variabila = some_variable, alta = my_fucking_list)

@app.route('/puppy/<name>')
def puppy(name):
    return "{}".format(name)

@app.route('/something')
def something():
    return render_template('something.html', variabila=[], alta=[])

@app.route('/something_else')
def something_else():
    return render_template('something_else.html', skanska = "Emanuel", variabila=[], alta=[])

@app.route('/thank_you')
def thank_you():
    first = request.args.get('first')
    return render_template('thank_you.html', skanska = "Emanuel", variabila=[], alta=[], first=first)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    


class InfoForm(FlaskForm):
    breed = StringField("What breed are you?")
    submit = SubmitField('Submit')
    
class InfoForm2(FlaskForm):
    breed2 = StringField('What breed2 are you?', validators=[DataRequired()])
    neutered = BooleanField('Have you been neutered?')
    mood = RadioField('Please choose your mood:', 
                      choices=[('mood_one','Happy'), ('mood_two', 'Excited')])
    food_choice = SelectField(u'Pick your favorite food:',
                              choices=[('chi', 'Chicken'), ('bf', 'Beef')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')
    
    

@app.route('/forms1', methods=['GET', 'POST'])
def forms1():
    breed = False 
    
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f"You just changed your breed to: {session['breed']}")
        breed = form.breed.data
        form.breed.data = ''
    return render_template('forms1.html', form=form, breed=breed)
    
@app.route('/forms2', methods=['GET','POST'])
def forms2():
    form = InfoForm2()
    if form.validate_on_submit():
        session['breed2'] = form.breed2.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data 
        session['feedback'] = form.feedback.data   

        return redirect(url_for('thank_you2'))
        
    return render_template('forms2.html', form=form)
    

@app.route('/thank_you2')
def thank_you2():
    return render_template('thank_you2.html')
    

if __name__ == '__main__':
    app.run()