from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')
    # if request.method == 'POST':
    #     if request.form['button'] == 'Input':
    #         pass # do something
    #     elif request.form['submit_button'] == 'Do Something Else':
    #         pass # do something else
    #     else:
    #         pass # unknown
    # elif request.method == 'GET':
    #     return render_template('home.html', form=form)

#try adding '/config' to the url! :)
@app.route('/config')
def config():
    return render_template('config.html')

if __name__ == '__main__':
    app.run(debug=True)
