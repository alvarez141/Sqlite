import sqlite3

def Connection():
    con = sqlite3.connect('DB/db_prueba/users.db')
    cursor = con.cursor()
    return con, cursor

def CreateTable(connection, cursor, info = False):
    sentence = """
    CREATE TABLE IF NOT EXISTS users(
    ID INTEGER PRIMARY KEY NOT  NULL,
    USER TEXT NULL,
    LASTNAME TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    CLAVE TEXT NOT NULL
    );
    """
    cursor.execute(sentence)

    #cursor.execute("ALTER TABLE users ADD COLUMN EJEMPLO TEXT NOT NULL DEFAULT ''")
    #cursor.execute("ALTER TABLE users DROP COLUMN EJEMPLO")

    if info:
        cursor.execute("PRAGMA table_info(users);")
        columns = cursor.fetchall()
        for column in columns:
            print(column)
    connection.close()

def InserData(connection, cursor,data):
    # setence = """
    # INSERT INTO users (USER, LASTNAME, EMAIL, CLAVE)
    # VALUES ('1', 'daniel', 'daniel@sunprored.es', '1234')
    # """
    setence = """
    INSERT INTO users VALUES (?, ?, ?, ?, ?)
    """
    #cursor.execute(setence)
    # cursor.execute(setence, data)
    cursor.executemany(setence, data)
    connection.commit()
    connection.close()

def query_data(connection, cursor):
    ...


if __name__ == '__main__':
    Connection()