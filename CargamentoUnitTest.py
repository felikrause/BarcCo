import unittest
from Cargamento import Cargamento

class TestCargamento(unittest.TestCase):
    
    def setUp(self):
        self.cargamento = Cargamento("test.db")
    
    def test_insertar_cargamento(self):
        self.cargamento.InsertarCargamento("Test", 100)
        result = self.cargamento.MostrarCargamento()
        self.assertEqual(len(result), 1)

if __name__ == '__main__':
    unittest.main()