import math
import unittest

from quadrature import simpson, trapezoidal


class QuadratureTests(unittest.TestCase):
    def test_trapezoidal_integrates_linear_function(self):
        self.assertAlmostEqual(trapezoidal(lambda x: 2*x+1, 0, 2, 5), 6.0)

    def test_simpson_integrates_cubic(self):
        self.assertAlmostEqual(simpson(lambda x: x**3, 0, 1, 4), 0.25)

    def test_sine_refinement_reduces_error(self):
        for rule in (trapezoidal, simpson):
            with self.subTest(rule=rule.__name__):
                coarse = abs(rule(math.sin, 0, math.pi, 8) - 2)
                fine = abs(rule(math.sin, 0, math.pi, 16) - 2)
                self.assertLess(fine, coarse)

    def test_reversed_interval_changes_sign(self):
        for rule in (trapezoidal, simpson):
            with self.subTest(rule=rule.__name__):
                self.assertAlmostEqual(rule(math.exp, 1, 0, 8), -rule(math.exp, 0, 1, 8))

    def test_invalid_counts_are_rejected(self):
        for rule in (trapezoidal, simpson):
            for count in (0, -2, 2.5, True):
                with self.subTest(rule=rule.__name__, count=count):
                    with self.assertRaises(ValueError):
                        rule(math.sin, 0, 1, count)

    def test_simpson_rejects_odd_count(self):
        with self.assertRaises(ValueError):
            simpson(math.sin, 0, 1, 3)


if __name__ == '__main__':
    unittest.main()
