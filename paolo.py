from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def paolo_is_here():
    return render_template('hello.html')

@app.route('/log', methods=['GET', 'POST'])
def write_log():
    if request.method == 'POST':
        if request.is_json:
            print(request.json)
        else:
            print(request.data)
        return "What am I doing\n"
    else:
        return "Only POST for now...\n"
