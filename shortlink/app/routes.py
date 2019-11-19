from flask import render_template, flash, redirect, url_for, request
from app import app
from app.randomizer import short_random
from app.forms import SubmitForm
from app.models import Urls
from app import db

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    short_random_value = short_random()
    form = SubmitForm()
    if form.validate_on_submit():
        new_long_short = Urls(longurl=form.longurl.data, shorturl=short_random_value)
        db.session.add(new_long_short)
        db.session.commit()
        flash('Your new long url is xxx.com/{}'.format(short_random_value))
        return redirect(url_for('index'))
    elif request.method == 'GET':
        pass

    return render_template('index.html', title='Home', short_random_value=short_random_value, form=form)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


####
