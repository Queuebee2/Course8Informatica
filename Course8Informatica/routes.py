"""Route declaration."""
from flask import current_app as app
from flask import render_template
from Bio.Seq import Seq
from Bio import Entrez

Entrez.email = "milain.lambers@gmail.com"

# hmm?
from Course8Informatica import db

@app.route('/')
def home():
    print("Hello")
    """Landing page."""
    nav = [{'name': 'Home', 'url': '/'},
           {'name': 'database', 'url': '/database'},
           {'name': 'test biopython', 'url': '/test_biopython'}]
    return render_template('home.html',
                           nav=nav,
                           title="Jinja Demo Site",
                           description="Smarter page templates \
                                with Flask & Jinja.")
@app.route('/database')
def database_test():
    """db page"""
    nav = [{'name': 'Home', 'url': '/'},
           {'name': 'database', 'url': '/database'},
           {'name': 'test biopython', 'url': '/test_biopython'}]
    result = db.engine.execute('select * from gene limit 10;').fetchall()
    print(result)

    return render_template('database_test.html',
                           nav=nav,
                           title="database TEST page",
                           description="This is the database TEST page, ",
                           result=result)

@app.route('/test_biopython')
def test_biopython():
    """test something page"""
    nav = [{'name': 'Home', 'url': '/'},
           {'name': 'database', 'url': '/database'},
           {'name': 'test biopython', 'url': '/test_biopython'}]

    my_seq = Seq("CATGTAGACTAG")
    return render_template('home.html',
                           nav=nav,
                           title="testing biopython import page",
                           description="succesfully created a Seq object")


