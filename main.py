from DB.Connection import Connection, CreateTable, InserData, query_data

con , cursor = Connection()
# CreateTable(con, cursor, info=True)
# InserData(con, cursor)
data = [
        (3,'gabriel','alvarez', 'delgadillo-gabriel02@gmai.com',1234),
        (4,'fabiola','alvarez', 'degadillofabiola@gmail.com.es',1234),
    ]
#InserData(con, cursor, data)

result = query_data(con, cursor)
for row in result:
        print(f"ID: {row[0]}")
        print(f"USER: {row[1]}")
        print(f"EMAIL: {row[2]}")
result.close()
