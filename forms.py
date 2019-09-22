from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField, IntegerField, validators
from flask_bootstrap import Bootstrap #not needed anymore.. but may be good to keep for later!

class homePageForm(FlaskForm):
    submit = SubmitField("Let's start!")

class characterForm(FlaskForm):
    difficulty = RadioField('Starting Number of Credits', choices=[('1000', 'Easy (16 Skills Point Max)'),('500', 'Medium (12 Skills Point Max)'),('100', 'Hard (8 Skills Point Max)')])
    name = StringField("Your character's name")
    pilot = IntegerField("Pilot Skill Points")
    merchant = IntegerField("Merchant Skill Points")
    fighter = IntegerField("Fighter Skill Points")
    engineer = IntegerField("Engineer Skill Points")
    submit = SubmitField("Submit")