import calc
import unittest

class testCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,15),25)
        self.assertEqual(calc.add(10.22,15.31),25.53)
    def test_sub(self):
        self.assertEqual(calc.sub(20,10),20)
        self.assertEqual(calc.sub(40,20),20)

    def test_mul(self):
        self.assertEqual(calc.mul(2, 10), 20)
        self.assertEqual(calc.mul(40, 20), 800)

    def testdiv(self):
        self.assertEqual(calc.div(20, 10), 2)
        self.assertEqual(calc.div(40, 20), 2)


if __name__  == "__main__":
    unittest.main(verbosity=2)