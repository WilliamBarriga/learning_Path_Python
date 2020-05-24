#cristal box
import unittest
def mayordeEdad(edad):
    if edad >= 18:
        return True
    else:
        return False

class cristalTest(unittest.TestCase):
    def testmayorEdad(self):
        edad = 20
        resultado = mayordeEdad(edad)
        self.assertEqual(resultado, True)
    def testmenorEdad(self):
        edad = 15
        resultado = mayordeEdad(edad)
        self.assertEqual(resultado, False)
if __name__ == "__main__":
    unittest.main()