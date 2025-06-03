import mysql.connector as sql


def connect_to_db():
    connection = sql.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "rest"
    )


    if connection.is_connected():
        print("Connection to database successful.")

    return connection


if __name__ == "__main__":
    connect_to_db()

