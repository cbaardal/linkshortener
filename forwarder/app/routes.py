from flask import render_template, flash, redirect, url_for, request
from app import app
from app.models import Urls
from app import db

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/<shorturlinput>')
def redirect(shorturlinput):
    longurl = Urls.query.filter_by(shorturl=shorturlinput).first()
    longurl_var = {'longurl': longurl}
    if longurl == None:
        return render_template('index.html')
    else:
        return render_template('forwarder.html', longurl=longurl)
