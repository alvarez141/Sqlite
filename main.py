from DB.Connection import Connection, CreateTable, InserData

con , cursor = Connection()
# CreateTable(con, cursor, info=True)
# InserData(con, cursor)
data = [
        (3,'gabriel','alvarez', 'delgadillo-gabriel02@gmai.com',1234),
        (4,'fabiola','alvarez', 'degadillofabiola@gmail.com.es',1234),
    ]
InserData(con, cursor, data)
