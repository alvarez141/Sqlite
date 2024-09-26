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
    #cursor.execute ("ALTER TABLE users ADD COLUMN password TEXT NULL")
    #cursor.execute("ALTER TABLE users DROP COLUMN password")
    connection.commit()
    # connection.close()
def add_data(connection, cursos, dates):
    sentence = "INSERT INTO users VALUES(? , ? , ?)"
    cursos.executemany(sentence, dates)

    connection.commit()
    connection.close()

def QueryData(connection, cursor, id = None):
    sentence = f"SELECT id, name FROM users WHERE id  = {id}"
    result = cursor.execute(sentence)
    return result

if __name__ == '__main__':
    Connection()