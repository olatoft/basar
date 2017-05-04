from flask import (Flask, flash, redirect, render_template, request, session,
                   abort)

app = Flask(__name__)


@app.route('/')
def index():
    return 'hei'


@app.route('/draw')
def draw():
    return 'this is the draw page'


@app.route('/draw/<string:name>/')
def getPerson(name):
    sitat = ['Heisann og hoppsann lillebror',
             'å vera elle ikkje vera, namnet skjemme ingen',
             'Jau, jau, eg driv med sau']
    sitatet = sitat[1]
    return render_template('draw.html', **locals())


@app.route('/range')
def range():
    return render_template('range.html')

if __name__ == '__main__':
    app.run()
