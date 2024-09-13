import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('example.db')

# Crear un cursor
c = conn.cursor()

# Crear una tabla
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insertar datos en la tabla
c.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
c.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

# Guardar (commit) los cambios
conn.commit()

# Consultar datos
c.execute('SELECT * FROM users')
print(c.fetchall())

# Cerrar la conexión
conn.close()