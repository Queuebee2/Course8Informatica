"""Route declaration."""
from flask import current_app as app
from flask import render_template
<<<<<<< HEAD
from flask import request
from Course8Informatica import pubmedsearchtool as ps


=======
from flask import abort
>>>>>>> origin/develop


@app.route('/')
def home():
    """Landing page."""

    return render_template('home.html',
                           title="Jinja Demo Site",
                           description="Smarter page templates \
                                with Flask & Jinja.")
@app.route('/database')
def database():
    """database test page."""
    return render_template('database_test.html',
                           title="database page",
                           description="This is the database")

<<<<<<< HEAD
@app.route('/search', methods=['GET', 'POST'])
def search_test():
    "Search page"
    search_term = '((variant [tiab] OR variants [tiab] OR mutation [tiab] OR mutations [tiab] OR substitutions [tiab] OR substitution [tiab] ) AND ("loss of function" [tiab] OR "loss-of-function" [tiab] OR "haplo-insufficiency" [tiab] OR haploinsufficiency [tiab] OR "bi-allelic" [tiab] OR "biallelic" [tiab] OR recessive [tiab] OR homozygous [tiab] OR heterozygous [tiab] OR "de novo" [tiab] OR dominant [tiab] OR " X-linked" [tiab]) AND ("intellectual" [tiab] OR "mental retardation" [tiab] OR "cognitive" [tiab] OR "developmental" [tiab] OR "neurodevelopmental" [tiab]) AND “last 2 years”[dp] AND KDM3B) '
    if search_term != "":
        ids = ps.run_querry(search_term)
        results = ps.parse_ids(ids)
    return render_template('search.html',
                           description=results)
=======
@app.route('/crash_the_server')
def server_error_test():
    abort(500, "success")


@app.route('/test_module_import')
def module_import_test():

    # import something
    from mysql import connector
    if connector:
        module_imported = True
    else:
        module_imported = False
    return render_template('testing/module_import_test.html',
                           title="testing module imports",
                           module_output=module_imported)
>>>>>>> origin/develop
