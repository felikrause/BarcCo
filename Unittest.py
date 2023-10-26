import unittest

def login(usuario, contraseña):
      if usuario == 'admin' and contraseña == 'admin':
        return "Iniciaste sesion como Administrador"
      elif usuario == "admins" and contraseña == "admins":
        return "Usuario y contraseña incorrectas"
class test(unittest.TestCase):

  def test_Error(self):
    self.assertEqual("Usuario y contraseña incorrecta" ,login("admins", "admins"))

  def test_Validate(self):
    self.assertEqual("Iniciaste sesion como Administrador" ,login("admin", "admin"))




if __name__ == "__main__":
  unittest.main()