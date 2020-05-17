import mysql.connector

from Repository import Sql
from appsettings import Config


class PaymentRepository:
    def __init__(self):
        self.dbconfig = Config()

    def getPaymentModesForUser(self):
        conn = mysql.connector.connect(user=self.dbconfig.DB_USERNAME, password=self.dbconfig.DB_PASSWORD,
                                       host=self.dbconfig.DB_HOSTNAME, port=self.dbconfig.DB_PORT,
                                       database=self.dbconfig.DB_NAME)

        cursor = conn.cursor()
        query = Sql.SqlQueries.getAllPaymentModesForUser
        cursor.execute(query)
        result = []
        columns = tuple([d[0] for d in cursor.description])
        for row in cursor:
            result.append(dict(zip(columns, row)))
        cursor.close()
        conn.close()
        return result


    def completePaymentActivity(self, jsonRequest):
        conn = mysql.connector.connect(user=self.dbconfig.DB_USERNAME, password=self.dbconfig.DB_PASSWORD,
                                       host=self.dbconfig.DB_HOSTNAME, port=self.dbconfig.DB_PORT,
                                       database=self.dbconfig.DB_NAME)

        cursor = conn.cursor()
        query = Sql.SqlQueries.insertPaymentDetails.format(int(jsonRequest['userid']), int(jsonRequest['paymentMode']), float(jsonRequest['amount']), int(jsonRequest['numberOfTickets']))
        cursor.execute(query)
        query = Sql.SqlQueries.insertBookingDetails.format(int(jsonRequest['userid']), int(jsonRequest['slotId']))
        cursor.execute(query)
        result = cursor.rowcount
        if result > 0 and int(jsonRequest['paymentMode']) == 6:
            query = Sql.SqlQueries.updateWalletBalance.format(float(jsonRequest['amount']), int(jsonRequest['userid']))
            cursor.execute(query)
            updateResult = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()

        return result > 0 or updateResult > 0

        return result


    def getBookingDetails(self, userid):
        conn = mysql.connector.connect(user=self.dbconfig.DB_USERNAME, password=self.dbconfig.DB_PASSWORD,
                                       host=self.dbconfig.DB_HOSTNAME, port=self.dbconfig.DB_PORT,
                                       database=self.dbconfig.DB_NAME)

        cursor = conn.cursor()
        query = Sql.SqlQueries.getBookingDetails.format(userid)
        cursor.execute(query)
        result = []
        columns = tuple([d[0] for d in cursor.description])
        for row in cursor:
            result.append(dict(zip(columns, row)))
        cursor.close()
        conn.close()
        return result


    def getWalletDetails(self, userid):
        conn = mysql.connector.connect(user=self.dbconfig.DB_USERNAME, password=self.dbconfig.DB_PASSWORD,
                                       host=self.dbconfig.DB_HOSTNAME, port=self.dbconfig.DB_PORT,
                                       database=self.dbconfig.DB_NAME)

        cursor = conn.cursor()
        query = Sql.SqlQueries.getWalletDetails.format(userid)
        cursor.execute(query)
        result = []
        columns = tuple([d[0] for d in cursor.description])
        for row in cursor:
            result.append(dict(zip(columns, row)))
        cursor.close()
        conn.close()
        return result