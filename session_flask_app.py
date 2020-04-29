from flask import Flask, render_template, request, session
from flask_session import Session
#from cachelib.file import FileSystemCache
from werkzeug.contrib.cache import FileSystemCache
#from flask_session.__init__ import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/", methods=["GET","POST"])
def fn_index():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)
    return render_template("session_index.html", notes=notes)
