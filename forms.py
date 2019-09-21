from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField, IntegerField, validators
from flask_bootstrap import Bootstrap #not needed anymore.. but may be good to keep for later!

class homePageForm(FlaskForm):
    submit = SubmitField("Let's start!")

class characterForm(FlaskForm):
    difficulty = RadioField('Level of Difficulty', choices=[('16', 'Easy'),('12', 'Medium'),('8', 'Hard')])
    name = StringField("Your character's name")
    pilot = IntegerField("Pilot Skill Points")
    merchant = IntegerField("Merchant Skill Points")
    fighter = IntegerField("Fighter Skill Points")
    engineer = IntegerField("Engineer Skill Points")
    submit = SubmitField("Submit")

class characterinfoForm(FlaskForm):
    submit = SubmitField("Let's start!")