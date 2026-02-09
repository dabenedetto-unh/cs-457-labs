import unittest
from solutions.lab03.lab2_2 import *

class TestLab3(unittest.TestCase):

    def test_summary_stats(self):
        data = [10, 20, 30]
        mean, stdev = calculate_summary_stats(data)
        self.assertEqual(mean, 20.0)
        self.assertAlmostEqual(stdev, 8.1649658, places=5)

    def test_five_number_summary(self):
        data = [1, 2, 3, 4, 5, 6, 7]
        # Min=1, Q1=2, Med=4, Q3=6, Max=7
        result = get_five_number_summary(data)
        self.assertEqual(result, (1, 2, 4, 6, 7))

    def test_batch_min_max_scaler(self):
        data = [10, 20, 30, 40, 50]
        expected = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(batch_min_max_scaler(data), expected)

    def test_batch_sentiment_binner(self):
        scores = [2, 3.5, 5]
        expected = ["Low", "Medium", "High"]
        self.assertEqual(batch_sentiment_binner(scores), expected)

if __name__ == "__main__":
    unittest.main()