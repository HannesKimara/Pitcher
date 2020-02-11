from flask import render_template
from flask_login import login_required

from . import main

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/profile/<username>")
@login_required
def profile():
    return render_template("profile.html")