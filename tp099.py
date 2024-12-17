from fractionClasseOff import Fraction
import unittest


class FractionTestCase(unittest.TestCase):

    # Test de l'affichage du numérateur avec des valeurs positives
    def test_numerator_positive(self):
        self.assertEqual(str(Fraction(1, 2)), "1/2")
        self.assertEqual(str(Fraction(1, -5)), "-1/5")
        self.assertEqual(str(Fraction(1, -1)), "-1")
        self.assertEqual(str(Fraction(1, 3)), "1/3")

    # Test de l'affichage du numérateur avec des valeurs négatives
    def test_numerator_negative(self):
        self.assertEqual(str(Fraction(-1, 2)), "-1/2")
        self.assertEqual(str(Fraction(-5, 3)), "-5/3")
        self.assertEqual(str(Fraction(-1, 1)), "-1")
        self.assertEqual(str(Fraction(-1, 3)), "-1/3")

    # Test des fractions nulles
    def test_numerator_null(self):
        self.assertEqual(str(Fraction(0, 2)), "0")
        self.assertEqual(str(Fraction(0, -5)), "0")
        self.assertEqual(str(Fraction(0, -1)), "0")
        self.assertEqual(str(Fraction(0, 3)), "0")

    # Tests d'addition de fractions
    def test_addition(self):
        self.assertEqual(Fraction(1, 2) + Fraction(1, 2), Fraction(1, 1))
        self.assertEqual(Fraction(0, 2) + Fraction(1, 2), Fraction(1, 2))
        self.assertEqual(Fraction(-5, 2) + Fraction(5, -2), Fraction(-5, 1))
        self.assertEqual(Fraction(2, 3) + Fraction(5, 2), Fraction(19, 6))

    # Test de la soustraction de fractions
    def test_subtraction(self):
        self.assertEqual(Fraction(1, 2) - Fraction(1, 2), Fraction(0, 2))
        self.assertEqual(Fraction(1, -2) - Fraction(0, 2), Fraction(-1, 2))
        self.assertEqual(Fraction(2, 3) - Fraction(1, 2), Fraction(1, 6))
        self.assertEqual(Fraction(2, 4) - Fraction(1, 4), Fraction(1, 4))

    # Test de la multiplication de fractions
    def test_multiplication(self):
        self.assertEqual(Fraction(1, 2) * Fraction(1, 2), Fraction(1, 4))
        self.assertEqual(Fraction(1, 2) * Fraction(1, 4), Fraction(1, 8))
        self.assertEqual(Fraction(1, -2) * Fraction(1, 6), Fraction(-1, 12))
        self.assertEqual(Fraction(2, 6) * Fraction(0, 4), Fraction(0, 1))

    # Test de la division des fractions
    def test_truedivision(self):
        self.assertEqual(Fraction(1, 2) / Fraction(1, 2), Fraction(1, 1))
        self.assertEqual(Fraction(1, 2) / Fraction(1, 4), Fraction(2, 1))
        self.assertEqual(Fraction(1, -2) / Fraction(1, 6), Fraction(-3, 1))
        self.assertEqual(Fraction(2, 6) / Fraction(3, 4), Fraction(4, 9))

    # Test de division par zéro
    def test_division_zero(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2) / Fraction(0, 3)
        with self.assertRaises(ZeroDivisionError):
            Fraction(5, 8) / Fraction(0, 8)
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 4) / Fraction(0, 4)

    # Test de la puissance des fractions
    def test_power(self):
        self.assertEqual(pow(Fraction(1, 2), 0), Fraction(1, 1))
        self.assertEqual(pow(Fraction(1, -2), -1), Fraction(-2, 1))
        self.assertEqual(pow(Fraction(1, 2), -1), Fraction(2, 1))
        self.assertEqual(pow(Fraction(5, 3), -1), Fraction(3, 5))

    # Test de la puissance avec zéro
    def test_power_zero(self):
        with self.assertRaises(ZeroDivisionError):
            pow(Fraction(0, 3), -2)
        with self.assertRaises(ZeroDivisionError):
            pow(Fraction(0, 2), -1)

    # Test de l'égalité des fractions
    def test_is_equal(self):
        self.assertTrue(Fraction(1, 2) == Fraction(8, 16))
        self.assertTrue(Fraction(2, 4) == Fraction(1, 2))
        self.assertFalse(Fraction(1, 2) == Fraction(1, 4))
        self.assertFalse(Fraction(1, 3) == Fraction(2, 3))

    # Test de la conversion en float
    def test_float(self):
        self.assertEqual(float(Fraction(1, 2)), 0.5)
        self.assertEqual(float(Fraction(2, 3)), 0.6666666666666666)
        self.assertEqual(float(Fraction(0, 2)), 0)
        self.assertEqual(float(Fraction(1, -2)), -0.5)

    # Test si la fraction est égale à zéro
    def test_is_zero(self):
        self.assertFalse(Fraction(1, 2).is_zero())
        self.assertFalse(Fraction(2, 3).is_zero())
        self.assertTrue(Fraction(0, 2).is_zero())
        self.assertTrue(Fraction(0, 3).is_zero())

    # Test si la fraction est un entier
    def test_is_integer(self):
        self.assertFalse(Fraction(1, 2).is_integer())
        self.assertFalse(Fraction(6, 9).is_integer())
        self.assertTrue(Fraction(12, 3).is_integer())
        self.assertTrue(Fraction(4, 1).is_integer())

    # Test si la fraction est propre
    def test_is_proper(self):
        self.assertTrue(Fraction(1, 2).is_proper())
        self.assertTrue(Fraction(1, 3).is_proper())
        self.assertFalse(Fraction(8, 4).is_proper())
        self.assertFalse(Fraction(6, 2).is_proper())

    # Test si la fraction est une unité
    def test_is_unit(self):
        self.assertTrue(Fraction(1, 2).is_unit())
        self.assertFalse(Fraction(2, 3).is_unit())
        self.assertTrue(Fraction(1, 8).is_unit())
        self.assertFalse(Fraction(5, 2).is_unit())

    # Test si deux fractions sont adjacentes
    def test_is_adjacent_to(self):
        self.assertTrue(Fraction(1, 3).is_adjacent_to(Fraction(1, 4)))
        self.assertTrue(Fraction(3, 4).is_adjacent_to(Fraction(2, 3)))
        self.assertFalse(Fraction(1, 5).is_adjacent_to(Fraction(4, 5)))
        self.assertFalse(Fraction(1, 3).is_adjacent_to(Fraction(1, 5)))

    # Test d'une comparaison entre fractions (en utilisant la conversion en float)
    def test_comparison(self):
        self.assertTrue(float(Fraction(1, 2)) > float(Fraction(1, 3)))  
        self.assertTrue(float(Fraction(1, 3)) < float(Fraction(1, 2)))  
        self.assertTrue(float(Fraction(1, 2)) >= float(Fraction(1, 2))) 
        self.assertTrue(float(Fraction(1, 2)) <= float(Fraction(2, 4)))  
        self.assertTrue(float(Fraction(1, 2)) == float(Fraction(2, 4)))  


if __name__ == "__main__":
    unittest.main()
