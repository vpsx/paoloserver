from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def paolo_is_here():
    return render_template('hello.html')
