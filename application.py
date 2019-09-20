# Check out the link to this Github for more info!
# https://github.com/RachitBhargava99/Flask-Tutorials

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


@app.route('/', methods=['GET', 'POST'])
def home():
    fl_form = homePageForm()
    if fl_form.is_submitted():
        return redirect(url_for('character'))
    else: 
        return render_template('home.html', html_form=fl_form)
    
#try adding '/character' to the url! :)
@app.route('/character', methods=['GET', 'POST'])
def character():
    fl_form = characterForm()
    if fl_form.is_submitted():
        return redirect(url_for('character'))
    else:
        return render_template('character.html', html_form=fl_form)


#try adding '/characterinfo' to the url! :)
@app.route('/characterinfo', methods=['GET', 'POST'])
def characterinfo():
    fl_form = characterFormInfo()
    if fl_form.is_submitted():
        return redirect(url_for('character'))
    else:
        return render_template('character.html', html_form=fl_form)


class homePageForm(FlaskForm):
    submit = SubmitField("Let's Start!")

class characterForm(FlaskForm):
    name_field = StringField('Input')
    submit = SubmitField("Submit")

class characterFormInfo(FlaskForm):
    name_field = StringField('Input')
    submit = SubmitField("Submit")

if __name__ == '__main__':
    app.run(debug=True)