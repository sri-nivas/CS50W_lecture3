from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def fn_index():
    return render_template("index_inherit.html")

@app.route('/more')
def fn_more():
    return render_template("more_inherit.html")
