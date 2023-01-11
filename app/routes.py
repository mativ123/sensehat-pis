from flask import render_template, flash, redirect, url_for, request, jsonify
from app import app, db
from app.forms import Specs
from app.models import Pickle
from werkzeug.urls import url_parse

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home')

@app.route('/specs', methods=['GET', 'POST'])
def specs():
    form = Specs()
    if form.validate_on_submit():
        pick = Pickle(kml=form.kml.data, tankstrl=form.tanktStrl.data)
        db.session.add(pick)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('specs.html', title="Specefikationer", form=form)
