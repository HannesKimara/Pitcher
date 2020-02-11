from flask import render_template, abort
from flask_login import login_required

from . import main
from ..models import User

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