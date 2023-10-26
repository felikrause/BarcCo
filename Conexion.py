import sqlite3


class Conexion:

  def __init__(self, nombreBD):
    self.conexion = sqlite3.connect(nombreBD)
    self.cursor = self.conexion.cursor()

  def crearDB(self):
    self.CrearCargamento()

  def CrearCargamento(self):
    self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS CARGAMENTO (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      tipoCargamento VARCHAR(45),
      pesoTotal DOUBLE
      )
    ''')
    self.conexion.commit()

  def InsertarCargamento(self, tipoCargamento, pesoTotal):
    self.cursor.execute(
        "INSERT INTO CARGAMENTO (tipoCargamento, pesoTotal) VALUES (?, ?)",
        (tipoCargamento, pesoTotal))
    self.conexion.commit()

  def crear_barco(self):
    self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS BARCO(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      capacidadMaxima DOUBLE,
      capacidadTanque DOUBLE,
      FOREIGN KEY(cargamento_id) REFERENCES CARGAMENTO(id))
      )
    ''')
    self.conexion.commit()

  def MostrarCargamento(self):
    self.cursor.execute("SELECT * FROM CARGAMENTO ORDER BY pesoTotal DESC")
    cargamento = self.cursor.fetchall()
    return cargamento

  def MostrarCargamentoPorTipo(self):
    self.cursor.execute(
        "SELECT * FROM CARGAMENTO ORDER BY tipoCargamento DESC")
    cargamento = self.cursor.fetchall()
    return cargamento

  def CerrarBD(self):
    self.cursor.close()
    self.conexion.close()
