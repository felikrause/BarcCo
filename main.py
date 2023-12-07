from flask import Flask, redirect, render_template, request, url_for

from Barco import Barco
from Cargamento import Cargamento
from Conexion import Conexion
from Viaje import Viaje

app = Flask(__name__)

conexion = Conexion("mi_basede_datos.db")
conexion.CrearDB()

barco_instancia = Barco("mi_basede_datos.db")


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
    cargamento = Cargamento("mi_basede_datos.db")
    cargamento.InsertarCargamento(tipo_cargamento, peso_total)
    return redirect(url_for('menu'))
  return render_template('crear_cargamento.html')

@app.route('/mostrar_cargamentos')
def mostrar_cargamentos():
  cargamento = Cargamento("mi_basede_datos.db")
  cargamentos = cargamento.MostrarCargamento()
  return render_template('mostrar_cargamento.html', cargamentos=cargamentos)


@app.route('/mostrar_cargamentos_por_tipo')
def mostrar_cargamentos_por_tipo():
  cargamento = Cargamento("mi_basede_datos.db")
  cargamentos = cargamento.MostrarCargamentoPorTipo()
  return render_template('mostrar_cargamentos_por_tipo.html',
                         cargamentos=cargamentos)


@app.route('/crear_barco', methods=['GET', 'POST'])
def crear_barco():
  if request.method == 'POST':
    capacidad_maxima = 1000
    capacidad_tanque = float(request.form['capacidad_tanque'])
    cargamento_id = int(request.form['cargamento_id'])
    barco_seleccionado = Barco("mi_basede_datos.db")
    barco_seleccionado.CrearBarco(capacidad_maxima,
                                                    capacidad_tanque,
                                                    cargamento_id)
    return redirect(url_for('menu'))
  return render_template('crear_barco.html')


@app.route('/mostrar_barco')
def mostrar_barco():
  barcos = Barco("mi_basede_datos.db")
  barcos = barcos.MostrarBarcos()
  return render_template('mostrar_barco.html', barcos=barcos)


@app.route('/iniciar_viaje', methods=['GET', 'POST'])
def iniciar_viaje():
  if request.method == 'POST':
    barco = Barco("mi_basede_datos.db")
    mostrar_barco()
    id_barco = int(request.form['id_barco'])
    barco_seleccionado = barco.ObtenerBarcoPorId(id_barco)

    if barco_seleccionado:
      viaje = Viaje("mi_basede_datos.db", barco_seleccionado, None, None)

      lugar_salida = request.form['lugar_salida']
      lugar_llegada = request.form['lugar_llegada']

      viaje.asignar_lugares(lugar_salida, lugar_llegada)
      viaje.iniciar_viaje(id_barco, lugar_salida, lugar_llegada)
      return redirect(url_for('menu'))
  return render_template('form_iniciar_viaje.html')


@app.route('/mostrar_viajes')
def mostrar_viajes():
  viaje = Viaje("mi_basede_datos.db", None, None, None)
  viajes = viaje.mostrar_viaje()
  return render_template('mostrar_viajes.html', viajes=viajes)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
