import mysql.connector as sql
import __init__ as connect

try:
    connect.connect_to_db()
except Exception as e:
    print("An error occured:", e)

cursor = connect.connection.cursor()


def readAllRecords():
    query = "SELECT * FROM user;"
    cursor.execute(query)
    records = query.fetchall()

    return records

def getUserbyID():
    query = "SELECT * FROM user ORDER BY id ASC;"
    cursor.execute(query)
    records = query.fetchall()

    return records



