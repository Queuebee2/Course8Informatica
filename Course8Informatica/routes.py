"""Route declaration."""
from flask import current_app as app
from flask import render_template
from flask import abort


@app.route('/')
def home():
    """Landing page."""

    return render_template('home.html',
                           title="Jinja Demo Site",
                           description="Smarter page templates \
                                with Flask & Jinja.")
@app.route('/database')
def database_test():
    """database test page."""
    return render_template('home.html',
                           title="database page",
                           description="This is the database")

@app.route('/crash_the_server')
def server_error_test():
    abort(500, "success")