from flask import render_template

from . import auth

@auth.route("register/", methods = ['GET', 'POST'])
def register():
    return render_template("auth/register.html")