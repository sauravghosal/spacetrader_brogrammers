from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField, IntegerField, validators
from flask_bootstrap import Bootstrap #not needed anymore.. but may be good to keep for later!

class homePageForm(FlaskForm):
    submit = SubmitField("Start New Game!")

class characterForm(FlaskForm):
    difficulty = RadioField('Starting Number of Credits', choices=[('1000', 'Easy (16 Skill Points Max)'),('500', 'Medium (12 Skill Points Max)'),('100', 'Hard (8 Skill Points Max)')])
    name = StringField("Your character's name. Please make sure the name is not empty.")
    pilot = IntegerField("Pilot Skill Points")
    merchant = IntegerField("Merchant Skill Points")
    fighter = IntegerField("Fighter Skill Points")
    engineer = IntegerField("Engineer Skill Points")
    submit = SubmitField("Submit")