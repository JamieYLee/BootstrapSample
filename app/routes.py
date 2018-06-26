from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import LoginForm

@app.route('/')
@app.route('/index/')
def index():
    user = {'username' : 'World'}
    return render_template('index.html', user=user, title='Home Page')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash('Welcome, {}!'.format(login_form.email.data))
        return redirect(url_for('index'))

    return render_template('login.html', form=login_form)
