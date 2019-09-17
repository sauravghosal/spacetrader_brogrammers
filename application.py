# Check out the link to this Github for more info!
# https://github.com/RachitBhargava99/Flask-Tutorials

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False


@app.route('/', methods=['GET', 'POST'])
def home():
    fl_form = SubmitForm()
    if fl_form.is_submitted():
        return redirect(url_for('config'))
    else: 
        return render_template('home.html', html_form=fl_form)
    
#try adding '/config' to the url! :)
@app.route('/character')
def config():
    return render_template('config.html')

class SubmitForm(FlaskForm):
    submit = SubmitField("SUBMIT")

if __name__ == '__main__':
    app.run(debug=True)