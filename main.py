import pymysql

class Database: 
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '12345',
            db = 'software_2'
        )

        self.cursor = self.connection.cursor()

        print("Conexion establecida correctamente")

database = Database()