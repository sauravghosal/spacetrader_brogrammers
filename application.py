""" This file contains the page redirection and some of the back-end logic for our game! """

from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap  #not needed anymore.. but may be good to keep for later!
from Game import HomePageForm, Game
from Player import Player, PlayerForm
from Universe import UniverseForm

APP = Flask(__name__)
Bootstrap(APP)
APP.config['WTF_CSRF_ENABLED'] = False

# Game object - everything is in this object
GAME = Game()


@APP.route('/', methods=['GET', 'POST'])
def home():
    """ Displays home page with button to begin the Game """

    fl_form = HomePageForm()
    if fl_form.validate_on_submit():
        return redirect(url_for('character'))
    return render_template('home.html', html_form=fl_form)


@APP.route('/character', methods=['GET', 'POST'])
def character():
    """ Displays page for user to customize character and starts a new Game with provided inputs """

    fl_form = PlayerForm()
    if fl_form.validate_on_submit():
        if str(fl_form.name.data) != "":
            player_1 = Player(fl_form.pilot.data, fl_form.merchant.data,
                              fl_form.fighter.data, fl_form.engineer.data,
                              int(fl_form.difficulty.data), fl_form.name.data)
            if fl_form.difficulty.data == "1000":
                player_1.skill_level = 16
                GAME.start_game(player_1, 'Easy')
            elif fl_form.difficulty.data == "500":
                player_1.skill_level = 12
                GAME.start_game(player_1, 'Medium')
            else:
                player_1.skill_level = 8
                GAME.start_game(player_1, 'Hard')

            if GAME.player.checkPoints():
                return redirect(url_for('characterinfo'))
            else:
                return render_template(
                    'character.html',
                    html_form=fl_form,
                    html_message=
                    'Something is wrong with your entry. Please try again.')
    else:
        return render_template('character.html',
                               html_form=fl_form,
                               html_message='No errors detected')


@APP.route('/characterinfo', methods=['GET', 'POST'])
def characterinfo():
    """ Displays character information with button to travel to another region """

    fl_form = UniverseForm()
    if fl_form.validate_on_submit():
        return redirect(url_for('regions'))
    return render_template('characterinfo.html', game=GAME, html_form=fl_form)


@APP.route('/regions', methods=['GET', 'POST'])
def regions():
    """ Displays a page containing all the regions """

    if request.method == 'POST' and request.form.get('regions') is not None:
        new_region_index = request.form.get('regions')
        new_region = GAME.universe.find_region(int(new_region_index))
        if GAME.travel(new_region):
            return redirect(url_for('characterinfo'))
        else:
            return render_template(
                'regions.html',
                game=GAME,
                error="You don't have enough fuel to travel!")
    elif request.method == 'POST' and request.form.get('market') is not None:
        item_key = request.form.get('market')
        if not GAME.buy(item_key):
            return render_template(
                'regions.html',
                game=GAME,
                error="You don't have enough inventory to hold that shit.")
    return render_template('regions.html', game=GAME, error="None")


if __name__ == '__main__':
    APP.run(debug=True)
