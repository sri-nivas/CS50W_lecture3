from flask import Flask

app = Flask(__name__)

@app.route("/")
def index(name):
    return "<h1> Hello {}!! </h1>".format(name)


@app.route("/david")
def david():
    return "<h1> Hello David!! </h1>"

#''' env FLASK_APP=flask_application.py flask run '''
