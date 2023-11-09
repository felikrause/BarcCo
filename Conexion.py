
import sqlite3

class Conexion:
    def __init__(self, nombreBD):
        self.nombreBD = nombreBD
        self.IniciarBD()

    def IniciarBD(self):
        self.conexion = sqlite3.connect(self.nombreBD)
        self.cursor = self.conexion.cursor()

    def CrearDB(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS CARGAMENTO(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipoCargamento VARCHAR(45),
                pesoTotal DOUBLE
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS BARCO(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                capacidadMaxima DOUBLE,
                capacidadTanque DOUBLE,
                cargamento_id INTEGER,
                FOREIGN KEY(cargamento_id) REFERENCES CARGAMENTO(id)
            )
        ''')
        self.conexion.commit()

    def CerrarBD(self):
        self.cursor.close()
        self.conexion.close()
  
    def commit(self):
      self.conexion.commit()
