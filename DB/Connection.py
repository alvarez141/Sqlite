import sqlite3

def Connection():
    con = sqlite3.connect('DB/db_prueba/users.db')
    cursor = con.cursor()
    return con, cursor

def create_table(connection, cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER NULL,
            name TEXT NULL,
            email TEXT NULL
        )
    ''')
    connection.commit()
    connection.close()

if __name__ == '__main__':
    Connection()