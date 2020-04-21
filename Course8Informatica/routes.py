"""Route declaration."""
from flask import current_app as app
from flask import render_template




@app.route('/')
def home():
    print("Hello")
    """Landing page."""
    nav = [{'name': 'Home', 'url': '/'},
           {'name': 'database', 'url': '/database'},
           {'name': 'nothingyet', 'url': 'nothingyet'}]
    return render_template('home.html',
                           nav=nav,
                           title="Jinja Demo Site",
                           description="Smarter page templates \
                                with Flask & Jinja.")
@app.route('/database')
def database_test():
    """Landing page."""
    nav = [{'name': 'Home', 'url': 'https://example.com/1'},
           {'name': 'About', 'url': 'https://example.com/2'},
           {'name': 'Pics', 'url': 'https://example.com/3'}]
    return render_template('home.html',
                           nav=nav,
                           title="database page",
                           description="This is the database")


