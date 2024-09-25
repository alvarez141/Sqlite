import sqlite3
from DB.Connection import Connection, create_table, add_data

con , cursor = Connection()
create_table(con, cursor)
dates =[(4, 'Juan', ''), (5, 'Pedro', ''), (6, 'Maria', ''),(7, 'Jose', ''),(8, 'Luis', ''),(9, 'Ana', '')]
add_data(con, cursor, dates = dates)