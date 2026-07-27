import sqlite3

DATABASE_NAME = "lifeos.db"


def connect_database():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection


def create_table():

    connection = connect_database()

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activities(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        activity TEXT,

        timestamp TEXT,

        duration INTEGER,

        category TEXT,

        source TEXT

    )
    """)

    connection.commit()

    connection.close()


def insert_dataframe(dataframe):

    connection = connect_database()

    dataframe.to_sql(
        "activities",
        connection,
        if_exists="append",
        index=False
    )

    connection.commit()

    connection.close()