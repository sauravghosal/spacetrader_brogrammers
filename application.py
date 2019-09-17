from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "I don't know what I'm doing!"

if __name__ == '__main__':
    app.run()
