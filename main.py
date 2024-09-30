import sqlite3
from DB.Connection import Connection, create_table, add_data, QueryData, UpdateData

con , cursor = Connection()
# create_table(con, cursor)
# dates =[(4, 'Juan', ''), (5, 'Pedro', ''), (6, 'Maria', ''),(7, 'Jose', ''),(8, 'Luis', ''),(9, 'Ana', '')]
# add_data(con, cursor, dates = dates)
users = QueryData(con, cursor, 7)
for row in users:
    print(row)


UpdateData(con, cursor, 7, 'Jose Luis Ramirez')
updated_users = QueryData(con, cursor, 7)
for row in updated_users:
    print(row)