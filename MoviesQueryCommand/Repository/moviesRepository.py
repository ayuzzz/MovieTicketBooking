import MySQLdb.cursors
import mysql.connector
from mysql.connector.cursor import MySQLCursorDict

from Repository import Sql
from appsettings import Config


class MovieRepository:
    dbconfig = Config

    def getallmoviedetails(self):
        conn = mysql.connector.connect(user=Config.DB_USERNAME, password=Config.DB_PASSWORD,
                                      host=Config.DB_HOSTNAME, port=Config.DB_PORT,
                                      database=Config.DB_NAME)
        # cursor = conn.cursor()
        # query = Sql.SqlQueries.getAllMovies
        # cursor.execute(query)
        # movieList = cursor.fetchall()
        # cursor.close()
        # conn.close()

        cursor = conn.cursor()
        query = Sql.SqlQueries.getAllMovies
        cursor.execute(query)
        result = []
        columns = tuple([d[0] for d in cursor.description])
        for row in cursor:
            result.append(dict(zip(columns, row)))
        cursor.close()
        conn.close()
        return result

