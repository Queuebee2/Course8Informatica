from flask import current_app as app
from flask import render_template

@app.errorhandler(404)
def page_not_found(e):
    # Todo turn this into a reroute through routes
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(e):
    # Todo turn this into a reroute through routes
    return render_template('errors/500.html', error_message=e.description), 500


app.register_error_handler(404, page_not_found)
app.register_error_handler(500, server_error)