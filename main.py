import sqlite3
from DB.Connection import Connection, create_table

con , cursor = Connection()
create_table(con, cursor)