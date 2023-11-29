from flask import Flask, render_template, request, redirect, url_for, session
from Conexion import Conexion
from Barco import Barco
from Cargamento import Cargamento
from Viaje import Viaje

app = Flask(__name__)

conexion = Conexion("mi_basede_datos.db")
conexion.CrearDB()

barco_instancia = Barco("mi_basede_datos.db")
cargamento_instancia = Cargamento("mi_basede_datos.db")

@app.route('/')
def menu():
    return render_template('menu.html')
  
"""def ingresar_cargamento():
  tipo_cargamento = input("Ingrese el tipo de cargamento: ")
  peso_total = float(input("Ingrese el peso total del cargamento: "))
  cargamento_instancia.InsertarCargamento(tipo_cargamento, peso_total)"""
  
@app.route('/crear_cargamento', methods=['GET', 'POST'])
def crear_cargamento():
    if request.method == 'POST':
        tipo_cargamento = request.form['tipo_cargamento']
        peso_total = float(request.form['peso_total'])
        cargamento_instancia.InsertarCargamento(tipo_cargamento, peso_total)
        return redirect(url_for('menu'))
    return render_template('crear_cargamento.html')


"""def mostrar_cargamentos():
  global cargamento
  cargamentos = cargamento_instancia.MostrarCargamento()
  print("Cargamentos:")
  for cargamento in cargamentos:
    print(f"ID: {cargamento[0]}, Tipo:", {cargamento[1]}, "Peso Total:",
          {cargamento[2]})"""

@app.route('/mostrar_cargamentos')
def mostrar_cargamentos():
    cargamentos = cargamento_instancia.MostrarCargamento()
    return render_template('mostrar_cargamentos.html', cargamentos=cargamentos)

    
"""def mostrar_cargamentos_por_tipo():
  global cargamento
  cargamentos = cargamento_instancia.MostrarCargamentoPorTipo()
  print("Cargamentos:")
  for cargamento in cargamentos:
    print(f"ID: {cargamento[0]}, Tipo:", {cargamento[1]}, "Peso Total:",
          {cargamento[2]})"""

@app.route('/mostrar_cargamentos_por_tipo')
def mostrar_cargamentos_por_tipo():
    cargamentos = cargamento_instancia.MostrarCargamentoPorTipo()
    return render_template('mostrar_cargamentos_por_tipo.html', cargamentos=cargamentos)


"""def crear_barco():
  capacidad_maxima = float(input("Ingrese la capacidad máxima del barco: "))
  capacidad_tanque = float(
      input("Ingrese la capacidad del tanque del barco: "))
  cargamento_id = int(
      input("Ingrese el ID del cargamento asociado al barco: "))
  barco_seleccionado = barco_instancia.CrearBarco(capacidad_maxima,
                                                  capacidad_tanque,
                                                  cargamento_id)
  return barco_seleccionado"""

@app.route('/crear_barco', methods=['GET', 'POST'])
def crear_barco():
    if request.method == 'POST':
        capacidad_maxima= request.form['capacidad_maxima']
        capacidad_tanque = float(request.form['capacidad_tanque'])
        cargamento_id = int(request.form['cargamento_id'])
        barco_seleccionado=barco_instancia.CrearBarco(capacidad_maxima, capacidad_tanque, cargamento_id)
        return redirect(url_for('menu'))
    return render_template('crear_barco.html')

"""def mostrar_barco():
  global barco
  barcos = barco_instancia.MostrarBarcos()
  print("Barcos:")
  for barco in barcos:
    print(
        f"ID: {barco[0]}, Capacidad Máxima: {barco[1]}, Capacidad Tanque: {barco[2]}, Cargamento ID: {barco[3]}"
    )"""

@app.route('/mostrar_barco')
def mostrar_barco():
    barcos = barco_instancia.MostrarBarcos()
    return render_template('mostrar_barco.html', barcos=barcos)


"""def iniciar_viaje():
  mostrar_barco()
  global barco
  id_barco = int(input("Seleccione el ID del barco para el viaje: "))
  barco_seleccionado = barco_instancia.ObtenerBarcoPorId(id_barco)

  if barco_seleccionado:
    viaje = Viaje("mi_basede_datos.db", barco_seleccionado, None, None)

    lugar_salida = input("Ingrese el lugar de salida: ")
    lugar_llegada = input("Ingrese el lugar de llegada: ")

    viaje.asignar_lugares(lugar_salida, lugar_llegada)
    viaje.iniciar_viaje(id_barco, lugar_salida, lugar_llegada)
  else:
    print("Barco no encontrado.")"""

@app.route('/iniciar_viaje', methods=['GET', 'POST'])
def iniciar_viaje():
    if request.method == 'POST':
        mostrar_barco()
        id_barco = int(request.form['id_barco'])
        barco_seleccionado = barco_instancia.ObtenerBarcoPorId(id_barco)

        if barco_seleccionado:
            viaje = Viaje("mi_basede_datos.db", barco_seleccionado, None, None)

            lugar_salida = request.form['lugar_salida']
            lugar_llegada = request.form['lugar_llegada']

            viaje.asignar_lugares(lugar_salida, lugar_llegada)
            viaje.iniciar_viaje(id_barco, lugar_salida, lugar_llegada)

    return render_template('form_iniciar_viaje.html')

"""def mostrar_viajes():
  viaje = Viaje("mi_basede_datos.db", None, None, None)
  viajes = viaje.mostrar_viaje()
  print("Viajes:")
  for v in viajes:
    print(
        f"ID Viaje: {v[0]}, Barco ID: {v[1]}, Lugar Salida: {v[3]}, Lugar Llegada: {v[4]}"
    )"""

@app.route('/mostrar_viajes')
def mostrar_viajes():
    viaje = Viaje("mi_basede_datos.db", None, None, None)
    viajes = viaje.mostrar_viaje()
    return render_template('mostrar_viajes.html', viajes=viajes)

"""
def main():
  while True:
    print("---Menu---")
    print("1. Crear Cargamento")
    print("2. Mostrar cargamentos por peso")
    print("3. Mostrar cargamento por tipo de cargamento ascendente")
    print("4. Crear barco")
    print("5. Mostrar barco")
    print("6. Iniciar Viaje")
    print("7. Mostrar Viajes")
    print("8. Salir")
    opcion = input("Ingrese la opción que desea realizar: " )
   
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
      iniciar_viaje()
    elif opcion == "7":
      mostrar_viajes()
    elif opcion == "8":
      conexion.CerrarBD()
      break
    else:
      print("Opción no válida. Por favor, seleccione una opción válida.")"""


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
