import random
from flask_wtf import FlaskForm
from wtforms import SubmitField
from abc import ABC, abstractmethod


class NPC(ABC):
    @abstractmethod
    def Interaction(self, game, option):
        pass


class NPCForm(FlaskForm):
    submit = SubmitField("Select!")