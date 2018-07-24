import MySQLdb
# import mysql.connector


class Database:

    host = 'localhost'
    user = 'sim'
    password = 'sim123'
    db = 'simsilsilah'

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        # self.connection = mysql.connector.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except ValueError:
            self.connection.rollback()

    def query(self, query):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)
        return cursor.fetchall()

    def getall(self, query):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)
        return cursor.fetchall()

    def getone(self, query):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)
        row = cursor.fetchall()
        x = 0
        c = None
        for r in row:
            x += 1
            c = r
            if x is 1:
                break
        if c is not None:
            return c

    def getone2(self, query):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)
        row = cursor.fetchone()
        if row is not None:
            return row['id']

    def count(self, query):
        cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)
        return cursor.rowcount

    def __del__(self):
        self.connection.close()
