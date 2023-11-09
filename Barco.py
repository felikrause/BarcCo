
from Conexion import Conexion
from Cargamento import Cargamento

class Barco:
    def IniciarBD(self):
      self.conexion = Conexion(self.nombreBD)
      self.cursor = self.conexion.cursor

    def __init__(self, nombreBD):
        self.nombreBD = nombreBD
        self.IniciarBD()
        self.cargamento = Cargamento(self.nombreBD)  

    def CrearBarco(self, capacidadMaxima, capacidadTanque, cargamento_id):
        self.cursor.execute(
          "INSERT INTO BARCO (capacidadMaxima, capacidadTanque, cargamento_id) VALUES (?, ?, ?)",
          (capacidadMaxima, capacidadTanque, cargamento_id))
        self.conexion.commit()

    def MostrarBarcos(self):
        self.cursor.execute("SELECT * FROM BARCO")
        barcos = self.cursor.fetchall()
        return barcos


    def ObtenerBarcoPorId(self, barco_id):
      self.cursor.execute("SELECT * FROM BARCO WHERE id = ?", (barco_id,))
      barco_by_id = self.cursor.fetchall()
      return barco_by_id