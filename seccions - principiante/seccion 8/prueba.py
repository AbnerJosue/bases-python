import unittest
from cambiaTexto import todo_mayusculas


class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = 'Buen dia'
        resultado = todo_mayusculas(palabra)
        self.assertEqual(resultado, 'BUEN DIA')

if __name__ == '__main__': 
    unittest.main()
