# Since I have to add getters/setters, it becomes really long, so let's split up the classes
# into individual files

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField, IntegerField
from ship import ship


class player:
    #Instance variables
    skill_level = 0

    def __init__(self, pilot, merchant, fighter, engineer, credits, name):
        self.pilot = pilot
        self.merchant = merchant
        self.fighter = fighter
        self.engineer = engineer
        self.credits = credits
        self.name = name
        self.ship = Ship()

    def check_points(self):
        return self.pilot + self.merchant + self.fighter + self.engineer <= self.skill_level

    # Setting the current Region (travel feature) - can just do p1.current_region = {new region}


# Form class
class PlayerForm(FlaskForm):
    difficulty = RadioField(
        'Starting Number of Credits',
        choices=[("1000", 'Easy (16 Skill Points Max)'),
                 ("500", 'Medium (12 Skill Points Max)'),
                 ("100", 'Hard (8 Skill Points Max)')],
    )
    name = StringField(
        "Your character's name. Please make sure the name is not empty.")
    pilot = IntegerField("Pilot Skill Points")
    merchant = IntegerField("Merchant Skill Points")
    fighter = IntegerField("Fighter Skill Points")
    engineer = IntegerField("Engineer Skill Points")
    submit = SubmitField("Submit")
