import sqlite3
from DB.Connection import Connection, create_table, add_data

con , cursor = Connection()
# create_table(con, cursor)
dates =[('1', 'Juan', ''), ('2', 'Pedro', ''), ('3', 'Maria', ''),(4, 'Jose', ''),(5, 'Luis', ''),(6, 'Ana', '')]
add_data(con, cursor, dates = dates)