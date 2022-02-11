import os.path

from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')
@app.route('/', methods = ['GET', 'POST'])

def index():
    return render_template('index.html')

@app.route('/ans', methods = ['GET', 'POST'])
def ans():
    if request.method =='POST':
        base = os.path.dirname(__file__)
        filepath = os.path.join()
