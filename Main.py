from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)


@app.route('/')
def index():
    return 'hei'


@app.route('/draw')
def draw():
    return 'this is the draw page'


@app.route('/draw/<string:name>/')
def getPerson(name):
    return render_template('draw.html', name=name)

if __name__ == '__main__':
    app.run()
