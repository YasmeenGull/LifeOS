import sqlite3

DATABASE = "lifeos.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def create_logs_table():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            activity TEXT,

            duration INTEGER,

            category TEXT

        )
    """)

    connection.commit()
    connection.close()


def insert_log(activity, duration, category):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO logs(activity,duration,category)
        VALUES(?,?,?)
        """,
        (
            activity,
            duration,
            category
        )
    )

    connection.commit()
    connection.close()
def get_logs():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, activity, duration, category
        FROM logs
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows

def create_goals_table():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS goals(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            goal TEXT,

            target INTEGER

        )
    """)

    connection.commit()
    connection.close()


def insert_goal(goal, target):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO goals(goal,target)
        VALUES(?,?)
        """,
        (
            goal,
            target
        )
    )

    connection.commit()
    connection.close()


def get_goals():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM goals")

    rows = cursor.fetchall()

    connection.close()

    return rows