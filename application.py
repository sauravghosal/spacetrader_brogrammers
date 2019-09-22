# Check out the link to this Github for more info!
# https://github.com/RachitBhargava99/Flask-Tutorials

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, RadioField
from forms import characterForm, homePageForm
from flask_bootstrap import Bootstrap #not needed anymore.. but may be good to keep for later!

app = Flask(__name__)
Bootstrap(app)
app.config['WTF_CSRF_ENABLED'] = False


@app.route('/', methods=['GET', 'POST'])
def home():
    fl_form = homePageForm()
    if fl_form.validate_on_submit():
        return redirect(url_for('character'))
    else: 
        return render_template('home.html', html_form=home_form)
    
#try adding '/character' to the url! :)
@app.route('/character', methods=['GET', 'POST'])
def character():
    fl_form = characterForm()
    if fl_form.validate_on_submit():
        # level = fl_form.difficulty.data 
        # need to figure out point validation
        maxSkillPoints = 0
        if (fl_form.difficulty.data == "1000"):
            maxSkillPoints = 16
        elif (fl_form.difficulty.data == "500"):
            maxSkillPoints = 12
        else:
            maxSkillPoints = 8
        if (int(fl_form.pilot.data) + int(fl_form.merchant.data) + int(fl_form.fighter.data) + int(fl_form.engineer.data) <= maxSkillPoints):
            return render_template('characterinfo.html', html_form=fl_form)
        else:
            return render_template('character.html', html_form=fl_form)
    else:
        return render_template('character.html', html_form=character_form)


if __name__ == '__main__':
    app.run(debug=True)