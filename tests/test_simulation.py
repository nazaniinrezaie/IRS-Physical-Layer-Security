import unittest
import numpy as np
from src.simulation import simulate


class SimulationTests(unittest.TestCase):
    def test_shapes_and_reproducibility(self):
        a = simulate(steps=80, seed=7)
        b = simulate(steps=80, seed=7)
        for x, y in zip(a, b):
            self.assertEqual(x.shape, (80, 2))
            np.testing.assert_array_equal(x, y)

    def test_filter_reduces_error_in_reference_case(self):
        truth, observations, estimates = simulate()
        self.assertLess(np.mean((estimates - truth)**2), np.mean((observations - truth)**2))


if __name__ == '__main__':
    unittest.main()
