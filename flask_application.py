from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return "<h1> Hello World!! </h1>"


#@app.route("/david")
#def david():
#    return "<h1> Hello David!! </h1>"


@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h2>Hello, {name}</h2>"


#''' env FLASK_APP=flask_application.py flask run '''
