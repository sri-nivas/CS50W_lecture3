from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> Hello World!! </h1>"


@app.route("/david")
def david():
    return "<h1> Hello David!! </h1>"

#''' env FLASK_APP=flask_application.py flask run '''
