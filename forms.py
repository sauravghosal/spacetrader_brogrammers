from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField, IntegerField
from flask_bootstrap import Bootstrap

class homePageForm(FlaskForm):
    submit = SubmitField("Let's start!")

class characterForm(FlaskForm):
    difficulty = RadioField('Level of Difficulty', choices=[('Easy','16 Skill Points'),('Medium','12 Skill Points'),('Hard','8 Skill Points')])
    name = StringField("Your character's name")
    pilot = IntegerField("Engineer Skill Points")
    merchant = IntegerField("Merchant Skill Points")
    fighter = IntegerField("Fighter Skill Points")
    engineer = IntegerField("Engineer Skill Points")
    submit = SubmitField("Submit")

