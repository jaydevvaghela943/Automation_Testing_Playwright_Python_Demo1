import pymysql


class DBManager:

    def connect(self):

        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="testdb"
        )

        return connection

    def execute_query(self, query):

        connection = self.connect()

        cursor = connection.cursor()

        cursor.execute(query)

        result = cursor.fetchall()

        connection.close()

        return result