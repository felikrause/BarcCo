from Conexion import Conexion
from Barco import Barco
from Cargamento import Cargamento

conexion = Conexion("mi_basede_datos.db")
conexion.CrearDB()

barco = Barco("mi_basede_datos.db")
cargamento = Cargamento("mi_basede_datos.db")


def ingresar_cargamento():
  tipo_cargamento = input("Ingrese el tipo de cargamento: ")
  peso_total = float(input("Ingrese el peso total del cargamento: "))
  cargamento.InsertarCargamento(tipo_cargamento, peso_total)


def mostrar_cargamentos():
  global cargamento
  cargamentos = cargamento.MostrarCargamento()
  print("Cargamentos:")
  for cargamento in cargamentos:
    print(f"ID: {cargamento[0]}, Tipo:", {cargamento[1]}, "Peso Total:", {cargamento[2]})


def mostrar_cargamentos_por_tipo():
  global cargamento
  cargamentos = cargamento.MostrarCargamentoPorTipo()
  print("Cargamentos:")
  for cargamento in cargamentos:
    print(f"ID: {cargamento[0]}, Tipo:", {cargamento[1]}, "Peso Total:", {cargamento[2]})

def crear_barco():
  capacidad_maxima = float(input("Ingrese la capacidad máxima del barco: "))
  capacidad_tanque = float(input("Ingrese la capacidad del tanque del barco: "))
  cargamento_id = int(input("Ingrese el ID del cargamento asociado al barco: "))
  barco.CrearBarco(capacidad_maxima, capacidad_tanque, cargamento_id)

def mostrar_barco():
  global barco
  barcos = barco.MostrarBarcos()
  print("Barcos:")
  for barco in barcos:
      print(f"ID: {barco[0]}, Capacidad Máxima: {barco[1]}, Capacidad Tanque: {barco[2]}, Cargamento ID: {barco[3]}")

# Menú principal

def main():
  while True:
    print("---Menu---")
    print("1. Crear Cargamento")
    print("2. Mostrar cargamentos por peso")
    print("3. Mostrar cargamento por tipo de cargamento ascendente")
    print("4. Crear barco")
    print("5. Mostrar barco")
    print("6. Salir")
    opcion = input("Ingrese la opción que desea realizar: ")

    if opcion == "1":
      ingresar_cargamento()
    elif opcion == "2":
      mostrar_cargamentos()
    if opcion == "3":
      mostrar_cargamentos_por_tipo()
    elif opcion == "4":
      crear_barco()
    elif opcion == "5":
      mostrar_barco()
    elif opcion == "6":
      conexion.CerrarBD()
      break
    else:
      print("Opción no válida. Por favor, seleccione una opción válida.")

main();