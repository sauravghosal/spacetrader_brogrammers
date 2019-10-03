from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField, IntegerField, validators
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap  #not needed anymore.. but may be good to keep for later!


class Region():
    def __init__(self, x, y, techLevel, name):
        self.x = x
        self.y = y
        self.techLevel = techLevel
        self.name = name
