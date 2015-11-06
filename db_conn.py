import mysql.connector
from mysql.connector import errorcode

"""
    Stores the db connection information 
    Contains functions to write to the db

    todo: separate connection parameters to a config file
"""
class db_conn:
    cnx = None

    def __init__(self):
        self.connect()

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(user='andrew', password='andrew',
                                          host='dev.findmine.us',
                                          database='andrew')

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
    def close(self):
        self.cnx.close()

    """ 
        Insert a row (url_from, url_to) to the link_edges table
        Note: does not check for duplicates (see _add_links_q)
    """
    def insert_link_edge(self, url_str, url_str_n):
        cursor = self.cnx.cursor()
        cursor.execute(self._add_links_q, (url_str, url_str_n));
        self.cnx.commit()
        cursor.close()

    _add_links_q = """
        INSERT into link_edges (url_from, url_to)
        VALUES (%s, %s);
    """
