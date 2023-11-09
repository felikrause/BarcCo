from Conexion import Conexion


class Cargamento:

  def __init__(self, nombreBD):
    self.nombreBD = nombreBD
    self.IniciarBD()

  def IniciarBD(self):
    self.conexion = Conexion(self.nombreBD)
    self.cursor = self.conexion.cursor

  def InsertarCargamento(self, tipoCargamento, pesoTotal):
    self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS CARGAMENTO(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipoCargamento VARCHAR(45),
                pesoTotal DOUBLE
            )
        ''')
    self.cursor.execute(
        "INSERT INTO CARGAMENTO (tipoCargamento, pesoTotal) VALUES (?, ?)",
        (tipoCargamento, pesoTotal))
    self.conexion.commit()

  def MostrarCargamento(self):
    self.cursor.execute("SELECT * FROM CARGAMENTO ORDER BY pesoTotal DESC")
    cargamento = self.cursor.fetchall()
    return cargamento

  def MostrarCargamentoPorTipo(self):
    self.cursor.execute("SELECT * FROM CARGAMENTO ORDER BY tipoCargamento ASC")
    cargamento = self.cursor.fetchall()
    return cargamento
