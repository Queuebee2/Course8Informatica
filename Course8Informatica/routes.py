"""Route declaration."""
from flask import current_app as app
from flask import render_template
from flask import request, Markup, Response
from Course8Informatica import pubmedsearchtool as ps
from Course8Informatica import gene_retriever as gr


from flask import abort


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
    # search_term = '((variant [tiab] OR variants [tiab] OR mutation [tiab] OR mutations [tiab] OR substitutions [tiab] OR substitution [tiab] ) AND ("loss of function" [tiab] OR "loss-of-function" [tiab] OR "haplo-insufficiency" [tiab] OR haploinsufficiency [tiab] OR "bi-allelic" [tiab] OR "biallelic" [tiab] OR recessive [tiab] OR homozygous [tiab] OR heterozygous [tiab] OR "de novo" [tiab] OR dominant [tiab] OR " X-linked" [tiab]) AND ("intellectual" [tiab] OR "mental retardation" [tiab] OR "cognitive" [tiab] OR "developmental" [tiab] OR "neurodevelopmental" [tiab]) AND “last 2 years”[dp] AND KDM3B) '
    collapsibles = ""
    search_term = request.form.get("search", "")
    marked = request.form.get("mark", "")
    export = request.form.get("export", "")

    print(request.form.getlist("checkbox"))

    if 'results' not in locals():
        results = ""

    if request.method == 'POST':
        if export == 'Export data':
            print(request.form.get("checkboxtest"))
            print(request.form.getlist("checkbox"))
            print("Export data")
            content = ""
            for i in range(10):
                checkbox = "checkbox{}".format(i)
                print(checkbox)
                print(request.form.get(checkbox, ""))
                if request.form.get("checkbox{}".format(i), "") == "on":
                    try:
                        print(i)
                        content += "{}".format(i)
                        # content += results[i]["TI"]
                    except KeyError:
                        pass
            print(content)
            return Response(
                content,
                mimetype="text/csv",
                headers={"Content-disposition":
                             "attachment; filename=db.csv"})

    if marked == 'Mark':
        print("Mark")
        for i in range(10):
            if request.form.get("checkbox" + str(i), "") == "on":
                print(i)
        return render_template('search.html',
                               description=Markup(collapsibles))

    if export != 'Export data' and marked != 'Mark':
        print("asdfasdfasdf")
        if search_term != "":
            results = ps.run_querry(search_term, 'abstract')
            collapsibles = ps.create_collapsible(results)
            table = ps.create_table(results)
            collapsibles = gr.mark_genes(collapsibles)
        # return render_template('search.html')
    return render_template('search.html',
                               description=Markup(collapsibles))

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
