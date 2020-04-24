"""Route declaration."""
from flask import current_app as app
from flask import render_template
from flask import request
from Course8Informatica import pubmedsearchtool as ps




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

@app.route('/search', methods=['GET', 'POST'])
def search_test():
    "Search page"
    search_term = '((variant [tiab] OR variants [tiab] OR mutation [tiab] OR mutations [tiab] OR substitutions [tiab] OR substitution [tiab] ) AND ("loss of function" [tiab] OR "loss-of-function" [tiab] OR "haplo-insufficiency" [tiab] OR haploinsufficiency [tiab] OR "bi-allelic" [tiab] OR "biallelic" [tiab] OR recessive [tiab] OR homozygous [tiab] OR heterozygous [tiab] OR "de novo" [tiab] OR dominant [tiab] OR " X-linked" [tiab]) AND ("intellectual" [tiab] OR "mental retardation" [tiab] OR "cognitive" [tiab] OR "developmental" [tiab] OR "neurodevelopmental" [tiab]) AND “last 2 years”[dp] AND KDM3B) '
    if search_term != "":
        ids = ps.run_querry(search_term)
        results = ps.parse_ids(ids)
    return render_template('search.html',
                           description=results)