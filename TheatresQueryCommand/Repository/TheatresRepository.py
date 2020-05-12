import mysql.connector
from mysql.connector.cursor import MySQLCursorDict

import Utility
from Repository import Sql
from appsettings import Config


class TheatreRepository:
    def __init__(self):
        self.dbconfig = Config()

    def getalltheatredetails(self):
        conn = mysql.connector.connect(user=self.dbconfig.DB_USERNAME, password=self.dbconfig.DB_PASSWORD,
                                       host=self.dbconfig.DB_HOSTNAME, port=self.dbconfig.DB_PORT,
                                       database=self.dbconfig.DB_NAME)
        cursor = conn.cursor()
        query = Sql.SqlQueries.getAllTheatres
        cursor.execute(query)
        result = []
        columns = tuple([d[0] for d in cursor.description])
        for row in cursor:
            result.append(dict(zip(columns, row)))
        cursor.close()
        conn.close()
        return result

    def insertSlotDetails(self, slotArray):
        slotValues = Utility.SqlUtility.convertList(slotArray)

        conn = mysql.connector.connect(user=self.dbconfig.DB_USERNAME, password=self.dbconfig.DB_PASSWORD,
                                       host=self.dbconfig.DB_HOSTNAME, port=self.dbconfig.DB_PORT,
                                       database=self.dbconfig.DB_NAME)
        cursor = conn.cursor()
        query = Sql.SqlQueries.insertSlotDetails.format(slotValues)
        cursor.execute(query)
        result = cursor.rowcount
        if(result > 0):
            query = Sql.SqlQueries.makeMovieLive.format(slotArray[0].MovieId)
            cursor.execute(query)
            updateResult = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()

        return result > 0 and updateResult > 0

    def getmoviebookingdetails(self, movieid):
        conn = mysql.connector.connect(user=self.dbconfig.DB_USERNAME, password=self.dbconfig.DB_PASSWORD,
                                       host=self.dbconfig.DB_HOSTNAME, port=self.dbconfig.DB_PORT,
                                       database=self.dbconfig.DB_NAME)
        cursor = conn.cursor()
        query = Sql.SqlQueries.getMovieBookingDetails.format(movieid)
        cursor.execute(query)
        result = []
        columns = tuple([d[0] for d in cursor.description])
        for row in cursor:
            result.append(dict(zip(columns, row)))
        cursor.close()
        conn.close()
        return result

    def getSlotDetailsForId(self, slotid):
        conn = mysql.connector.connect(user=self.dbconfig.DB_USERNAME, password=self.dbconfig.DB_PASSWORD,
                                       host=self.dbconfig.DB_HOSTNAME, port=self.dbconfig.DB_PORT,
                                       database=self.dbconfig.DB_NAME)
        cursor = conn.cursor()
        query = Sql.SqlQueries.getSlotDetailsForId.format(slotid)
        cursor.execute(query)
        result = []
        columns = tuple([d[0] for d in cursor.description])
        for row in cursor:
            result.append(dict(zip(columns, row)))
        cursor.close()
        conn.close()
        return result