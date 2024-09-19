import sqlite3

def Connection():
    con = sqlite3.connect('DB/db_prueba/user.db')
    cursor = con.cursor()
    return con, cursor

if __name__ == '__main__':
    Connection()