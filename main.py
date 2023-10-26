from Conexion import Conexion

conexion = Conexion("mi_basede_datos.db")
conexion.crearDB()


def ingresar_cargamento():
  tipo_cargamento = input("Ingrese el tipo de cargamento: ")
  peso_total = float(input("Ingrese el peso total del cargamento: "))
  conexion.InsertarCargamento(tipo_cargamento, peso_total)


def mostrar_cargamentos():
  cargamentos = conexion.MostrarCargamento()
  print("Cargamentos:")
  for cargamento in cargamentos:
    print("Tipo:", {cargamento[1]}, "Peso Total:", {cargamento[2]})


def mostrar_cargamentos_por_tipo():
  cargamentos = conexion.MostrarCargamentoPorTipo()
  print("Cargamentos:")
  for cargamento in cargamentos:
    print("Tipo:", {cargamento[1]}, "Peso Total:", {cargamento[2]})

# Menú principal

def main():
  while True:
    print("---Menu---")
    print("1. Crear Cargamento")
    print("2. Mostrar cargamentos por peso")
    print("3. Mostrar cargamento por tipo de cargamento ascendente")
    print("4. Salir")
    opcion = input("Ingrese la opción que desea realizar: ")

    if opcion == "1":
      ingresar_cargamento()
    elif opcion == "2":
      mostrar_cargamentos()
    elif opcion == "3":
      mostrar_cargamentos_por_tipo()
    elif opcion == "4":
      conexion.CerrarBD()
      break
    else:
      print("Opción no válida. Por favor, seleccione una opción válida.")

main();
