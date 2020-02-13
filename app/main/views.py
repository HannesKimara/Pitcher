from flask import render_template, abort, redirect, url_for, request
from flask_login import login_required, current_user

from . import main
from .forms import PitchForm, CommentForm
from ..models import User, Pitch, Comment

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
        pitch_save_id = new_pitch.save_pitch()

        return redirect(url_for("main.by_category", pitch_category = form.category.data))

    title = "Pitch | New Pitch"

    return render_template('add_pitch.html', form = form, title = title)

@main.route('/pitch/category/<pitch_category>')
def by_category(pitch_category):
    category_pitches = Pitch.query.filter_by(category = pitch_category).all()
    title = f"Pitch | {pitch_category}"

    return render_template('pitches.html', pitches = category_pitches, title = title)

@main.route('/pitch/view/<pitch_id>')
def view_pitch(pitch_id):
    curr_pitch = Pitch.query.filter_by(pitch_id = pitch_id).first()
    comments = Comment.query.filter_by(pitch_id = pitch_id).all()

    title = "Pitch"
    return render_template("pitch.html", pitch = curr_pitch, comments = comments, title = title)

@main.route('/comment/new/<pitch_id>', methods = ['GET', 'POST'])
@login_required
def comment(pitch_id):
    form = CommentForm()

    if form.validate_on_submit():
        curr_pitch = Pitch.query.filter_by(pitch_id = pitch_id).first()
        new_comment = Comment(content= form.content.data, pitch = curr_pitch, user_id = current_user.user_id)
        save_comment_id = new_comment.save_comment()

        return redirect(url_for("main.view_pitch", pitch_id = pitch_id))

    title = "Pitch | Comment"

    return render_template("comment.html", form = form, pitch_id = pitch_id, title = title)

    
