from flask import render_template

from . import main

@main.app_errorhandler(404)
def error_404(error):
    '''
    Function to render the 404 error page
    '''
    title = "404 | Page not Found"

    return render_template('errors/404.html', title = title), 404

@main.app_errorhandler(500)
def error_500(error):
    '''
    Function to render the 500 error page
    '''
    title = "500 | Server Error"

    return render_template('errors/500.html', title = title), 500

@main.app_errorhandler(405)
def error_405(error):
    '''
    Function to render the 500 error page
    '''
    title = "405 | Method Not Allowed"

    return render_template('errors/405.html', title = title), 405