"""Route declarations."""
import re

from flask import current_app as app
from flask import render_template
from flask import request, Response, redirect
from Course8Informatica import pubmedsearchtool as ps
from Course8Informatica import gene_retriever as gr
from Course8Informatica import csv_formatter as cf
from Course8Informatica.file_reader import test_is_filename_updated, update_filename, GENEPANEL_FILENAME
from werkzeug.utils import secure_filename

from flask import abort

requestdata = ""


@app.route('/')
@app.route('/home')
def home():
    """Homepage"""
    return render_template('index.html')


@app.route('/update_genepanel', methods=['GET', 'POST'])
def update():
    """
    Method called upon clicking update-genepanel button
    checks whether a file has been selected, if so, checks whether the file
    already exists.
    If the file is new, it is saved on the server to be used as
    genpanel.

    TODO's:
        1. Could: return (append) warning / popup ...
        2. Should: Compare hashes of newly uploaded file and existing
        3. Should: Validate the genepanel file
        4. Must: (Make sure) genepanel contents are re-loaded!

    :return: redirect request back to /search
    """
    if request.method == 'POST':
        file = request.files['file']
        if file:
            print(f'saving {file.filename}')

            if file.filename == GENEPANEL_FILENAME:
                print(f"user tried to upload duplicate of existing genepanel")
                # TODO 1. return (append) warning / popup ...
                # "If that's the newest genepanel, you're already up to date!"
                # TODO 2. (actually compare the hash of both to be sure)
                return redirect("/search", code=302)

            # TODO 3. validate the genepanel file
            # if <some error> do something

            file.save(secure_filename(file.filename))

            # update the filename global (dirty hack -_-)
            update_filename(file.filename)

            # TODO 4. make sure genepanel contents are re-loaded!
            #  (see gene_retriever)
            print(f'filename updated to: {test_is_filename_updated()}')
        else:
            # TODO 5. return (append) warning / popup ...
            # "You tried to update the genepanel but no file was chosen!"
            print('no file selected')

    # back to search page
    return redirect("/search", code=302)


@app.route('/search', methods=['GET', 'POST'])
def search_test():
    """
    Search page

    :return:
    """
    global requestdata

    search = ['', '', '', '', '']
    search[0] = request.form.get("search1", "")
    search[1] = request.form.get("search2", "")
    search[2] = request.form.get("search3", "")
    search[3] = request.form.get("search4", "")
    search[4] = request.form.get("search5", "")
    marked = request.form.get("select", "")
    selectall = request.form.get("select-all", "")
    deselectall = request.form.get("deselect-all", "")
    export = request.form.get("export", "")
    update = request.form.get("update", "")

    collapsible_data = requestdata
    print(requestdata)

    if request.method == 'POST':
        if export == 'Export data':
            print(request.form.getlist("checkbox"))
            content = "PMID;Gene(s);Title\n"
            for i in range(len(collapsible_data)):
                if request.form.get(f"checkbox{i}", "") == "on":
                    PMID = collapsible_data[i][3]
                    genes = gr.find_genes(collapsible_data[i])
                    title = collapsible_data[i][0]
                    content += cf.format_csv_data(PMID, genes, title) + '\n'
            return Response(content,mimetype="text/csv",
                            headers={
                                "Content-disposition":
                                "attachment; filename=gene_results.csv"
                            })

        if marked == 'Select':
            print("Mark")
            for i in range(10):
                if request.form.get("checkbox" + str(i), "") == "on":
                    print(i)

        if selectall == "Select all":
            return render_template('search.html',
                                   results=collapsible_data, mark="checked")

        if deselectall == "De-select all":
            return render_template('search.html',
                                   results=collapsible_data, mark="")

    if search[0] or search[1] or search[2]:
        results = ps.run_query(search, 'abstract')
        collapsible_data = ps.create_collapsible(results)
        collapsible_data = gr.find_genes(collapsible_data)
        if request.form.get("checkbox_phenotype", "") == "on":
            collapsible_data = gr.find_mesh_terms(collapsible_data)
        requestdata = collapsible_data
    return render_template('search.html',
                           results=collapsible_data)

@app.route('/crash_the_server')
def server_error_test():
    """ tests whether server error 500 is correctly handled """
    abort(500, "success")


@app.route('/test_module_import')
def module_import_test():
    """ Test if arbitrary module (that initially caused issues)
    is properly imported on request
    """
    from mysql import connector
    if connector:
        module_imported = True
    else:
        module_imported = False
    return render_template('testing/module_import_test.html',
                           title="testing module imports",
                           module_output=module_imported)
