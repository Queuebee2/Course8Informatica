""""
DbConnector
Datum: 25-04-2020
Auteur: Bart Jolink
"""

import mysql.connector
from datetime import date


class DbConnector:
    def __init__(self):
        self.connection = self.set_connection()

    def insert_info(self, info):
        """"This function inserts information into the database.
        Input is info.
        """

        db_info = self.retrieve_info(info)
        if db_info is None:
            cursor = self.connection.cursor(buffered=True)
            cursor.execute(
                "insert into <db field>"
                "values(null, '{}');"
                .format(info))
            self.connection.commit()
            cursor.close()

    def retrieve_info(self, identifier):
        """"This function retrieves certain information from the database.
        Input is a identiefier.
        Output are results.
        """

        cursor = self.connection.cursor(buffered=True)

        cursor.execute(
            "select <info> "
            "from <tabel> "
            "where identifier = ( select <info> "
            "                       from <tabel> "
            "                       where identifier = '{}'"
            "                       limit 1);".format(
                identifier))
        results = cursor.fetchone()
        cursor.close()

        return results

    def update_info(self, identifier):
        """"This function updates information in the database.
        Input is identifier (and date/time?)
        """
        today = date.today()

        cursor = self.connection.cursor(buffered=True)
        cursor.execute(
            "UPDATE information "
            "SET last_update = '{}' "
            "where seq_id = '{}';"
                .format(today, identifier))
        self.connection.commit()
        cursor.close()

    def set_connection(self):
        """"This function sets a connection to a database (Ossux).
        Output is an SQL_connection.
        """

        sql_connection = mysql.connector.connect(
            host="hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com",
            user="owe7_pg4@hannl-hlo-bioinformatica-mysqlsrv",
            db="Owe7_pg4",
            password="blaat1234")

        return sql_connection

