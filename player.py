# Since I have to add getters/setters, it becomes really long, so let's split up the classes
# into individual files

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField, IntegerField, validators
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap  #not needed anymore.. but may be good to keep for later!


class Player:
    #Instance variables
    current_region = None
    credits = 0
    max_skill_points = 0
    difficulty = None

    def __init__(self, pilot, merchant, fighter, engineer):
        self.pilot = pilot
        self.merchant = merchant
        self.fighter = fighter
        self.engineer = engineer
        self.credits = credits

    def check_difficulty(self, credits):
        if (credits == "1000"):
            max_skill_points = 16
            difficulty = 'Easy'
        elif (credits == "500"):
            max_skill_points = 12
            difficulty = 'Medium'
        else:
            max_skill_points = 8
            difficulty = 'Hard'

        if (self.pilot + self.merchant + self.fighter + self.engineer <=
                max_skill_points):
            self.credits = int(credits)
            self.max_skill_points = max_skill_points
            self.difficulty = difficulty
            return True
        else:
            return False

    # Setting the current Region (travel feature) - can just do p1.current_region = {new region}


# Form class
class playerForm(FlaskForm):
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