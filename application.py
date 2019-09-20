# Check out the link to this Github for more info!
# https://github.com/RachitBhargava99/Flask-Tutorials

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


@app.route('/', methods=['GET', 'POST'])
def home():
    home_form = homePageForm()
    if home_form.is_submitted():
        return redirect(url_for('character'))
    else: 
        return render_template('home.html', html_form=home_form)
    
#try adding '/character' to the url! :)
@app.route('/character', methods=['GET', 'POST'])
def character():
    character_form = characterForm()
    if character_form.is_submitted():
        return redirect(url_for('confirmation'))
    else:
        return render_template('character.html', html_form=character_form)


#try adding '/characterinfo' to the url! :)
@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    confirmation_form = confirmationForm()
    if confirmation_form.is_submitted():
        return redirect(url_for('character'))
    else:
        return render_template('confirmation.html', html_form=confirmation_form)


class homePageForm(FlaskForm):
    submit = SubmitField("Let's Start!")

class characterForm(FlaskForm):
    name_field = StringField('Input')
    submit = SubmitField("Submit")

class confirmationForm(FlaskForm):
    name_field = StringField('Input')
    submit = SubmitField("Submit")

if __name__ == '__main__':
    app.run(debug=True)