
from Conexion import Conexion
class Viaje:

  def __init__(self, nombreBD, barco_id, lugar_salida, lugar_llegada):
    self.barco_id = barco_id
    self.lugar_salida = lugar_salida
    self.lugar_llegada = lugar_llegada
    self.nombreBD = nombreBD
    self.IniciarBD()

  def IniciarBD(self):
    self.conexion = Conexion(self.nombreBD)
    self.cursor = self.conexion.cursor

  def asignar_lugares(self, lugar_salida, lugar_llegada):
    self.lugar_salida = lugar_salida
    self.lugar_llegada = lugar_llegada

  def iniciar_viaje(self, barco_id, lugar_salida, lugar_llegada):
    self.barco_id = barco_id
    self.lugar_salida = lugar_salida
    self.lugar_llegada = lugar_llegada
    self.cursor.execute(
      "INSERT INTO VIAJE (barco_id, lugar_salida, lugar_llegada) VALUES (?, ?, ?)",
      (self.barco_id, self.lugar_salida, self.lugar_llegada))
    self.conexion.commit()

  def mostrar_viaje(self):
    self.cursor.execute("SELECT * FROM VIAJE")
    viaje = self.cursor.fetchall()
    return viaje
  

  
    