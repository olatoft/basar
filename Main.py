from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)
import validation
import drawer

app = Flask(__name__)


@app.route('/')
def index():
    return 'hei'


@app.route('/draw')
def draw():
    lower = int(session['lower'])
    upper = int(session['upper'])
    random_number = str(drawer.get_random_number(lower, upper))
    return render_template('draw.html', **locals())


@app.route('/test/<string:name>/')
def getPerson(name):
    sitat = ['Heisann og hoppsann lillebror',
             'å vera elle ikkje vera, namnet skjemme ingen',
             'Jau, jau, eg driv med sau']
    sitatet = sitat[1]
    return render_template('draw.html', **locals())


@app.route('/range', methods=['GET', 'POST'])
def range():
    if request.method == 'POST':
        lower = request.form['lower']
        upper = request.form['upper']
        if validation.is_valid_form(lower, upper):
            session['lower'] = str(lower)
            session['upper'] = str(upper)
            return redirect(url_for('draw'))
    return render_template('range.html')

app.secret_key = """\x19D\xb95\x1a0\x83\x12\xb8\x182\x90\x90\xc9i\r\x9d1\xbe
                    \xf8\x96\x9f\x8e\x17"""

if __name__ == '__main__':
    app.run()
