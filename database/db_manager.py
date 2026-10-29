import pymysql


class DBManager:

    def connect(self):

        return pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="testdb"
        )

    def fetch(self, query):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute(query)

        result = cursor.fetchall()

        connection.close()

        return result