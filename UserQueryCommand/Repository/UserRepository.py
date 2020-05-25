import mysql.connector

from Repository import Sql
from appsettings import Config


class UserRepository:
    def __init__(self):
        self.dbconfig = Config()

    def getUserDetails(self, userid):
        conn = mysql.connector.connect(user=self.dbconfig.DB_USERNAME, password=self.dbconfig.DB_PASSWORD,
                                       host=self.dbconfig.DB_HOSTNAME, port=self.dbconfig.DB_PORT,
                                       database=self.dbconfig.DB_NAME)

        cursor = conn.cursor()
        query = Sql.SqlQueries.getUserDetails.format(userid)
        cursor.execute(query)
        result = []
        columns = tuple([d[0] for d in cursor.description])
        for row in cursor:
            result.append(dict(zip(columns, row)))
        cursor.close()
        conn.close()
        return result


    def submitUserDetails(self, jsonRequest):
        conn = mysql.connector.connect(user=self.dbconfig.DB_USERNAME, password=self.dbconfig.DB_PASSWORD,
                                       host=self.dbconfig.DB_HOSTNAME, port=self.dbconfig.DB_PORT,
                                       database=self.dbconfig.DB_NAME)

        cursor = conn.cursor()
        query = Sql.SqlQueries.submitUserDetails.format(jsonRequest['firstName'], jsonRequest['lastName'], jsonRequest['primaryContact']
                                                        , jsonRequest['country'], jsonRequest['city'], jsonRequest['paymentMode']
                                                        , jsonRequest['age'], jsonRequest['userid'])

        cursor.execute(query)
        result = cursor.rowcount > 0
        cursor.close()
        conn.commit()
        conn.close()
        return result

    def validateUsernamePassword(self, username_password):
        conn = mysql.connector.connect(user=self.dbconfig.DB_USERNAME, password=self.dbconfig.DB_PASSWORD,
                                       host=self.dbconfig.DB_HOSTNAME, port=self.dbconfig.DB_PORT,
                                       database=self.dbconfig.DB_NAME)

        cursor = conn.cursor()
        query = Sql.SqlQueries.validateUser.format(username_password['userName'], username_password['password'])

        cursor.execute(query)
        result = []
        columns = tuple([d[0] for d in cursor.description])
        for row in cursor:
            result.append(dict(zip(columns, row)))
        cursor.close()
        conn.close()
        return result