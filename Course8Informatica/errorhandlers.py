from flask import current_app as app
from flask import render_template

@app.errorhandler(404)
def page_not_found(e):
    """Handles 404 requests, renders code 404 error page"""
    # Todo turn this into a reroute through routes
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(e):
    """Handles 500 requests, renders code 500 error page"""
    # Todo turn this into a reroute through routes
    return render_template('errors/500.html'), 500


# register error handlers to app
app.register_error_handler(404, page_not_found)
app.register_error_handler(500, server_error)