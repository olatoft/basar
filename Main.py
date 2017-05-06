from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'hei'


@app.route('/draw')
def draw():
    return session['lower'] + session['upper']


@app.route('/draw/<string:name>/')
def getPerson(name):
    sitat = ['Heisann og hoppsann lillebror',
             'å vera elle ikkje vera, namnet skjemme ingen',
             'Jau, jau, eg driv med sau']
    sitatet = sitat[1]
    return render_template('draw.html', **locals())


@app.route('/range', methods=['GET', 'POST'])
def range():
    if request.method == 'POST':
        session['lower'] = request.form['lower']
        session['upper'] = request.form['upper']
        return redirect(url_for('draw'))
    else:
        return render_template('range.html')

app.secret_key = """\x19D\xb95\x1a0\x83\x12\xb8\x182\x90\x90\xc9i\r\x9d1\xbe
                    \xf8\x96\x9f\x8e\x17"""

if __name__ == '__main__':
    app.run()
