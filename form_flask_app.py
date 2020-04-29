from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def fn_index():
    return render_template('form_index.html')


@app.route('/hello', methods=['GET','POST'])
def fn_hello():
    if request.method == 'GET':
        return "Please submit the form instead"
    else:
        name = request.form.get('name')
        return render_template('form_hello.html', name=name)
