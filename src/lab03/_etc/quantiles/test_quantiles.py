import unittest
import random
import math
import pandas as pd
import statistics as stats

from week3.etc_quantiles.quantiles import *

class TestQuartiles(unittest.TestCase):

    def test_known_even_sequence(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8]
        # n=8, mid=4. low=[1,2,3,4] (med 2.5), high=[5,6,7,8] (med 6.5), total med 4.5
        q1, q2, q3 = quartiles_medians(data)
        self.assertAlmostEqual(q1, 2.5)
        self.assertAlmostEqual(q2, 4.5)
        self.assertAlmostEqual(q3, 6.5)

    def test_known_odd_sequence(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # n=9, mid=4. low=[1,2,3,4] (med 2.5), high=[6,7,8,9] (med 7.5), total med 5.0
        q1, q2, q3 = quartiles_medians(data)
        self.assertAlmostEqual(q1, 2.5)
        self.assertAlmostEqual(q2, 5.0)
        self.assertAlmostEqual(q3, 7.5)

    def test_small_set(self):
        data = [10, 20, 30]
        q1, q2, q3 = quartiles_medians(data)
        self.assertEqual(q1, 10)
        self.assertEqual(q2, 20)
        self.assertEqual(q3, 30)

    def test_identical_values(self):
        data = [5] * 10
        q1, q2, q3 = quartiles_medians(data)
        self.assertEqual(q1, 5)
        self.assertEqual(q2, 5)
        self.assertEqual(q3, 5)

    def test_random_divby4_vs_pandas(self):
        data = [random.randint(0, 100) for _ in range(20)]
        summary = quartiles_medians(data)
        series = pd.Series(data)
        q1 = series.quantile(0.25, interpolation='midpoint')
        q2 = series.quantile(0.5, interpolation='midpoint')
        q3 = series.quantile(0.75, interpolation='midpoint')
        
        for s, q in zip(summary, [q1, q2, q3]):
            self.assertAlmostEqual(s, q)

    def test_singly_even_vs_pandas(self):

        data = [random.randint(0, 100) for _ in range(18)]
        summary = quartiles_medians(data)
        series = pd.Series(data)
        # each half is odd
        q1 = series.quantile(0.25, interpolation='lower')     
        q2 = series.quantile(0.5, interpolation='midpoint') 
        q3 = series.quantile(0.75, interpolation='higher')   
        
        for s, q in zip(summary, [q1, q2, q3]):
            self.assertAlmostEqual(s, q)

    def test_random_odd_vs_stats(self):
        data = [random.randint(0, 100) for _ in range(21)]
        summary = quartiles_medians(data)

        qts = stats.quantiles(data)
        
        for s, q in zip(summary, qts):
            self.assertAlmostEqual(s, q)

if __name__ == "__main__":
    unittest.main()
