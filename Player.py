# Since I have to add getters/setters, it becomes really long, so let's split up the classes
# into individual files

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField, IntegerField
from Ship import Ship


class Player:
    #Instance variables
    skill_level = 0

    def __init__(self, pilot, merchant, fighter, engineer, credits, name):
        self.pilot = pilot
        self.merchant = merchant
        self.fighter = fighter
        self.engineer = engineer
        self.credits = credits
        self.name = name
        self.karma = 50
        self.ship = Ship()

    def checkPoints(self):
        return self.pilot + self.merchant + self.fighter + self.engineer <= self.skill_level

    def getKarma(self):
        return self.karma
    
    def addKarma(self, amount):
        if self.karma == 100 or self.karma + amount == 100:
            self.karma = 100
        else:
            self.karma = self.karma + amount

    def loseKarma(self, amount):
        if self.karma == 0 or self.karma - amount == 0:
            self.karma = 0
        else:
            self.karma = self.karma - amount


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
