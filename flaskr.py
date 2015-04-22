#all the imports
from flask import Flask, request, session, redirect, url_for, \
     abort, render_template, flash

# configuration

DEBUG = True
SECRET_KEY = 'any key for test'
USERNAME = 'admin'
PASSWORD = 'default'


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('success'))
    return render_template('login.html', error=error)   


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))    


if __name__ == '__main__':
    app.run()