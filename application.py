# Check out the link to this Github for more info!
# https://github.com/RachitBhargava99/Flask-Tutorials

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField
from Game import homePageForm, Game
from flask_bootstrap import Bootstrap  #not needed anymore.. but may be good to keep for later!
from Player import Player, playerForm
from Universe import Universe, UniverseForm

app = Flask(__name__)
Bootstrap(app)
app.config['WTF_CSRF_ENABLED'] = False

# Game object - everything is in this object
game = Game()


@app.route('/', methods=['GET', 'POST'])
def home():
    fl_form = homePageForm()
    if fl_form.validate_on_submit():
        return redirect(url_for('character'))
    else:
        return render_template('home.html', html_form=fl_form)


@app.route('/character', methods=['GET', 'POST'])
def character():
    fl_form = playerForm()
    if fl_form.validate_on_submit():
        if (str(fl_form.name.data) != ""):
            p1 = Player(fl_form.pilot.data, fl_form.merchant.data,
                        fl_form.fighter.data, fl_form.engineer.data,
                        int(fl_form.difficulty.data), fl_form.name.data)
            if (fl_form.difficulty.data == "1000"):
                p1.skill_level = 16
                game.startGame(p1, 'Easy')
            elif (fl_form.difficulty.data == "500"):
                p1.skill_level = 12
                game.startGame(p1, 'Medium')
            else:
                p1.skill_level = 8
                game.startGame(p1, 'Hard')

            if (game.player.checkPoints()):
                return redirect(url_for('characterinfo'))
            else:
                return render_template(
                    'character.html',
                    html_form=fl_form,
                    html_message=
                    'Something is wrong with your entry. Please try again.'
                )
    else:
        return render_template('character.html',
                               html_form=fl_form,
                               html_message='No errors detected')


# Redirection for region page still needs to be implemented


@app.route('/characterinfo', methods=['GET', 'POST'])
def characterinfo():
    fl_form = UniverseForm()
    if fl_form.validate_on_submit():
        return redirect(url_for('regions'))
    else:
        return render_template('characterinfo.html',
                               game=game,
                               html_form=fl_form)


@app.route('/regions', methods=['GET', 'POST'])
def regions():
    if request.method == 'POST' and request.form.get('regions') != None:
        new_region_index = request.form.get('regions')
        game.curr_region = game.universe.find_region(int(new_region_index))
        return redirect(url_for('characterinfo'))
    else:
        return render_template('regions.html', game=game)


if __name__ == '__main__':
    app.run(debug=True)