#black box
import unittest
def suma(num1, num2):
    return num1 + num2

class cajaNegraTest(unittest.TestCase):
    def testSumaPositiva(self):
        num1 = 10
        num2 = 5
        resultado = suma(num1, num2)
        self.assertEqual(resultado, 15)
    def testSumaNegativa(self):
        num1 = -10
        num2 = -7
        resultado = suma (num1, num2)
        self.assertEqual(resultado, -17)

if __name__ == "__main__":
    unittest.main()

        