import unittest
from Conexion import Conexion

class TestConexion(unittest.TestCase):
    def setUp(self):
        self.conexion = Conexion(":memory:")

    def tearDown(self):
        self.conexion.CerrarBD()

    def test_crear_cargamento(self):
        self.conexion.CrearCargamento()
        

    def test_insertar_cargamento(self):
        self.conexion.CrearCargamento()
        self.conexion.InsertarCargamento("Carga1", 100.0)
        

    def test_mostrar_cargamento(self):
        self.conexion.CrearCargamento()
        self.conexion.InsertarCargamento("Carga1", 100.0)
        cargamento = self.conexion.MostrarCargamento()
        

if __name__ == '__main__':
    unittest.main()