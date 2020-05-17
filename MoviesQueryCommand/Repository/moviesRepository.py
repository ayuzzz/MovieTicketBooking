import mysql.connector
from mysql.connector.cursor import MySQLCursorDict

from Repository import Sql
from appsettings import Config


class MovieRepository:
    def __init__(self):
        self.dbconfig = Config()

    def getallmoviedetails(self):
        conn = mysql.connector.connect(user=self.dbconfig.DB_USERNAME, password=self.dbconfig.DB_PASSWORD,
                                            host=self.dbconfig.DB_HOSTNAME, port=self.dbconfig.DB_PORT,
                                            database=self.dbconfig.DB_NAME)
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

    def getNonLiveMovies(self):
        conn = mysql.connector.connect(user=self.dbconfig.DB_USERNAME, password=self.dbconfig.DB_PASSWORD,
                                       host=self.dbconfig.DB_HOSTNAME, port=self.dbconfig.DB_PORT,
                                       database=self.dbconfig.DB_NAME)
        cursor = conn.cursor()
        query = Sql.SqlQueries.getNonLiveMovies
        cursor.execute(query)
        result = []
        columns = tuple([d[0] for d in cursor.description])
        for row in cursor:
            result.append(dict(zip(columns, row)))
        cursor.close()
        conn.close()
        return result

    def getmoviedetails(self, movieid, userid):
        conn = mysql.connector.connect(user=self.dbconfig.DB_USERNAME, password=self.dbconfig.DB_PASSWORD,
                                       host=self.dbconfig.DB_HOSTNAME, port=self.dbconfig.DB_PORT,
                                       database=self.dbconfig.DB_NAME)
        cursor = conn.cursor()
        query = Sql.SqlQueries.getMovieDetails.format(movieid, userid)
        cursor.execute(query)
        result = []
        columns = tuple([d[0] for d in cursor.description])
        for row in cursor:
            result.append(dict(zip(columns, row)))
        cursor.close()
        conn.close()
        return result

    def addToWishlist(self, movieid, userid):
        conn = mysql.connector.connect(user=self.dbconfig.DB_USERNAME, password=self.dbconfig.DB_PASSWORD,
                                       host=self.dbconfig.DB_HOSTNAME, port=self.dbconfig.DB_PORT,
                                       database=self.dbconfig.DB_NAME)
        cursor = conn.cursor()
        query = Sql.SqlQueries.addToWishlist.format(movieid, userid)
        cursor.execute(query)
        result = cursor.rowcount > 0
        conn.commit()
        cursor.close()
        conn.close()
        return result


    def getWishlistedMovies(self, userid):
            conn = mysql.connector.connect(user=self.dbconfig.DB_USERNAME, password=self.dbconfig.DB_PASSWORD,
                                           host=self.dbconfig.DB_HOSTNAME, port=self.dbconfig.DB_PORT,
                                           database=self.dbconfig.DB_NAME)
            cursor = conn.cursor()
            query = Sql.SqlQueries.getWishlist.format(userid)
            cursor.execute(query)
            result = []
            columns = tuple([d[0] for d in cursor.description])
            for row in cursor:
                result.append(dict(zip(columns, row)))
            cursor.close()
            conn.close()
            return result