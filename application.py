# Check out the link to this Github for more info!
# https://github.com/RachitBhargava99/Flask-Tutorials

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField
from forms import homePageForm
from flask_bootstrap import Bootstrap  #not needed anymore.. but may be good to keep for later!
from player import Player, playerForm

app = Flask(__name__)
Bootstrap(app)
app.config['WTF_CSRF_ENABLED'] = False


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
    if fl_form.validate_on_submit():  #validate_on_submit is not working...
        p1 = Player(fl_form.pilot.data, fl_form.merchant.data,
                    fl_form.fighter.data, fl_form.engineer.data)
        if ((str(fl_form.name.data) != "")
                and p1.check_difficulty(fl_form.difficulty.data)):
            return render_template('characterinfo.html',
                                   html_form=fl_form,
                                   html_difficulty=p1.difficulty)
        else:
            # maybe add a flash() functionality here?
            return render_template(
                'character.html',
                html_form=fl_form,
                html_message=
                'Something is wrong with your submission. Please try again.')
    else:
        return render_template('character.html',
                               html_form=fl_form,
                               html_message='No errors detected')


if __name__ == '__main__':
    app.run(debug=True)