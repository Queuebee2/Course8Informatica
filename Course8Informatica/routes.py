"""Route declaration."""
import re

from flask import current_app as app
from flask import render_template
from flask import request, Response, after_this_request
from Course8Informatica import pubmedsearchtool as ps
from Course8Informatica import gene_retriever as gr
from Course8Informatica import csv_formatter as cf

from flask import abort

requestdata = ""

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


@app.route('/search', methods=['GET', 'POST'])
def search_test():
    "Search page"

    global requestdata

    # search_term = '((variant [tiab] OR variants [tiab] OR mutation [tiab] OR mutations [tiab] OR substitutions [tiab] OR substitution [tiab] ) AND ("loss of function" [tiab] OR "loss-of-function" [tiab] OR "haplo-insufficiency" [tiab] OR haploinsufficiency [tiab] OR "bi-allelic" [tiab] OR "biallelic" [tiab] OR recessive [tiab] OR homozygous [tiab] OR heterozygous [tiab] OR "de novo" [tiab] OR dominant [tiab] OR " X-linked" [tiab]) AND ("intellectual" [tiab] OR "mental retardation" [tiab] OR "cognitive" [tiab] OR "developmental" [tiab] OR "neurodevelopmental" [tiab]) AND “last 2 years”[dp] AND KDM3B) '
    search_term = request.form.get("search", "")
    marked = request.form.get("mark", "")
    markall = request.form.get("mark-all", "")
    unmarkall = request.form.get("unmark-all", "")
    export = request.form.get("export", "")

    collapsible_data = requestdata
    print(requestdata)

    if request.method == 'POST':
        if export == 'Export data':
            print(request.form.getlist("checkbox"))
            content = "PMID;Gene(s);Title\n"
            for i in range(len(collapsible_data)):
                if request.form.get("checkbox{}".format(i), "") == "on":
                    PMID = collapsible_data[i][3]
                    genes = gr.find_genes(collapsible_data[i])
                    title = collapsible_data[i][0]
                    content += cf.format_csv_data(PMID, genes,
                                                  title) + '\n'
            return Response(
                content,
                mimetype="text/csv",
                headers={"Content-disposition":
                             "attachment; filename=gene_results.csv"})

        if marked == 'Mark':
            print("Mark")
            for i in range(10):
                if request.form.get("checkbox" + str(i), "") == "on":
                    print(i)

    if search_term != "":
        results = ps.run_querry(search_term, 'abstract')
        collapsible_data = ps.create_collapsible(results)
        collapsible_data = gr.find_genes(collapsible_data)
        requestdata = collapsible_data
    return render_template('search.html',
                           results=collapsible_data)


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
