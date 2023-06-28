import mysql.connector

class conexion:
    def __init__(self, host, user, password, database):
        self.host = host,
        self.user = user,
        self.password= password,
        self.database = database,
        self.conexion = None
        self.cursor = None

    def connect(self):
        self.conexion = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
        )
        self.cursor = self.conexion.cursor()
        if self.conexion.is_connected():
            print("Conexión exitosa")

midb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "dupe",
    database = "proyectointegrador")
print(midb)

cursor = midb.cursor()
cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)