
import unittest
import numpy as np

from src.irs_optimization import (
    secrecy_rate,
    optimize_irs,
)


class IRSOptimizationTests(unittest.TestCase):

    def test_nonnegative_secrecy_rate(self):
        rate = secrecy_rate(1 + 1j, 0.5 + 0.2j)
        self.assertGreaterEqual(rate, 0)

    def test_optimization_not_worse_than_baseline(self):
        baseline, optimized, phases = optimize_irs(
            num_elements=16,
            trials=2000,
            seed=42,
        )

        self.assertGreaterEqual(optimized, baseline)
        self.assertEqual(len(phases), 16)

    def test_reproducibility(self):
        result1 = optimize_irs(seed=42)
        result2 = optimize_irs(seed=42)

        self.assertAlmostEqual(result1[1], result2[1])
        np.testing.assert_allclose(
            result1[2],
            result2[2],
        )


if __name__ == "__main__":
    unittest.main()
