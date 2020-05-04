#from mysql.connector import connect
import mysql.connector
from flask import render_template, request

class EnsembleDbHandler():
    db_config = {
        'host': 'ensembldb.ensembl.org',
        'user': 'anonymous',
        'db': 'homo_sapiens_core_95_38'
    }

    def __init__(self):
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.db_config)
            self.cursor = self.connection.cursor()
            print('connected to ensemble db')           # todo use for logging
        except Exception as e:
            print(e)                                    # todo log
            # handle e

    def is_connected(self):
        return self.connection.is_connected()

    def do_query(self):
        self.cursor.execute("select * from gene limit 1;")
        results = self.cursor.fetchone()
        return results

    def init_app(self, app):

        @app.route("/database_test", methods=["POST", "GET"])
        def database_test_query():
            return render_template('testing/database_test.html')

        @app.route("/do-request", methods=["POST", "GET"])
        def do_something():
            if request.form['submit_button'] == "Do Something":
                print('pressed do something')
                result = self.do_query()
            elif request.form['submit_button'] == "Do Something Else":
                print('pressed do something else')
                result = 'no result'
            return render_template('testing/database_test.html', result=result)
