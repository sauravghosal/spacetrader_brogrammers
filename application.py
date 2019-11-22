""" This file contains the page redirection and some of the back-end logic for our game! """

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap  #not needed anymore.. but may be good to keep for later!
from Game import HomePageForm, Game, SubmitForm
from Player import Player, PlayerForm
from Universe import UniverseForm
from NPC import NPCForm
from Bandit import Bandit
from Police import Police
from Trader import Trader

APP = Flask(__name__)
Bootstrap(APP)
APP.config['WTF_CSRF_ENABLED'] = False
APP.config['SECRET_KEY'] = '3d6f45a5fc12445dbac2f59c3b6c7cb1'

# Game object - everything is in this object
GAME = Game()


@APP.route('/', methods=['GET', 'POST'])
def home():
    """ Displays home page with button to begin the Game """

    form = HomePageForm()
    if form.validate_on_submit():
        return redirect(url_for('character'))
    return render_template('index.html', form=form)


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
                return redirect(url_for('hub'))
            else:
                flash(u'Something went wrong. Please try again.', 'error')
                return render_template(
                    'character.html',
                    html_form=fl_form,
                )
    else:
        return render_template('character.html',
                               html_form=fl_form,
                               html_message='No errors detected')


@APP.route('/hub', methods=['GET', 'POST'])
def hub():
    """ Displays character information with button to travel to another region """
    if (GAME.player.ship.health <= 0):
        return redirect(url_for('end'))
    fl_form = UniverseForm()
    if fl_form.validate_on_submit():
        return redirect(url_for('regions'))
    return render_template('hub.html', game=GAME, html_form=fl_form)


@APP.route('/regions', methods=['GET', 'POST'])
def regions():
    """ Displays a page containing all the regions """
    if request.method == 'POST' and request.form.get('refuel') is not None:
        if GAME.refuel():
            flash(u"Refueled up to 100", 'success')
        else:
            flash(u"Not enough credits to purchase fuel", 'error')
    if request.method == 'POST' and request.form.get('repair'):
        if GAME.repair():
            flash(u"Repaired up to 100", 'success')
        else:
            flash(u"Not enough credits to repair", 'error')
    if request.method == 'POST' and request.form.get('regions') is not None:
        new_region_index = request.form.get('regions')
        new_region = GAME.universe.find_region(int(new_region_index))
        if GAME.travel(new_region):
            GAME.encounter()
            if GAME.npc != None:
                return redirect(
                    url_for('encounter', region_index=new_region_index))
            return redirect(url_for('hub'))
        else:
            flash(u"You can't travel there!", 'error')
    elif request.method == 'POST' and request.form.get('market') is not None:
        item_key = request.form.get('market')
        if GAME.buy(item_key):
            if item_key == 'universe':
                return render_template('win.html')
            flash(u"Item bought!", 'success')
        else:
            flash(u"You don't have enough inventory to hold that.", 'error')
    elif request.method == 'POST' and request.form.get(
            'inventory') is not None:
        item_key = request.form.get('inventory')
        GAME.loseItem(item_key)
    return render_template('market.html', game=GAME)


@APP.route('/encounter', methods=['GET', 'POST'])
def encounter():
    """ Encounter page """
    region_index = int(request.args.get('region_index', None))
    region = GAME.universe.find_region(region_index)
    if request.method == 'POST' and request.form.get('options') is not None:
        option = request.form.get('options')
        result = GAME.npc.Interaction(GAME, option)
        # this might be better changed....
        if result[0] == 'Not able to Negotiate':
            return redirect(url_for("trader"))
        GAME.curr_region = region
        return redirect(url_for('result', result=result[0]))
    else:
        return render_template('encounter.html', game=GAME)


@APP.route('/result', methods=['GET', 'POST'])
def result():
    fl_form = SubmitForm()
    result = request.args.get('result', None)
    if fl_form.validate_on_submit():
        return redirect(url_for('hub'))
    else:
        return render_template('encounter-result.html',
                               result=result,
                               html_form=fl_form)


@APP.route('/trader', methods=['GET', 'POST'])
def trader():
    if request.method == 'POST' and request.form.get('options') is not None:
        options = request.form.get('options')
        result = GAME.npc.Negotiate(GAME, options)
        return redirect(url_for('result', result=result))
    else:
        return render_template('trader.html', game=GAME)


@APP.route('/end', methods=['GET', 'POST'])
def end():
    form = HomePageForm()
    if form.validate_on_submit():
        return redirect(url_for('character'))
    return render_template('end.html', form=form)


if __name__ == '__main__':
    APP.run(debug=True)
