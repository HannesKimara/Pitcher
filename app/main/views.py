from flask import render_template, abort
from flask_login import login_required, current_user

from . import main
from .forms import PitchForm
from ..models import User, Pitch

@main.route("/")
def index():
    title = "Pitch"
    return render_template("index.html", title = title)

@main.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)

    title = "Pitch | Profile"
    return render_template("profile.html", user = user, title = title)

@main.route('/pitch/new', methods = ['GET', 'POST'])
@login_required
def newpitch():
    form = PitchForm()
    if form.validate_on_submit():
        new_pitch = Pitch(category = form.category.data, content = form.content.data, user=current_user)
        print(new_pitch.save_pitch())

    return render_template('add_pitch.html', form = form)

@main.route('/pitch/category/<pitch_category>')
def by_category(pitch_category):
    category_pitches = Pitch.query.filter_by(category = pitch_category).all()
    title = f"Pitch | {pitch_category}"

    return render_template('pitches.html', pitches = category_pitches, title = title)