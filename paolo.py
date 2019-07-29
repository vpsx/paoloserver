from flask import Flask
app = Flask(__name__)

@app.route('/')
def paolo_is_here():
    return "We\'re still looking. We\'ll keep you posted."
