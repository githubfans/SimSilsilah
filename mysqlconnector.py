import mysql.connector

config = {
    'user': 'sim',
    'password': 'sim123',
    'host': 'localhost',
    'database': 'simsilsilah',
    'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)

cnx.close()
