import unittest
from lab3_starter import *
import statistics

class TestLab3(unittest.TestCase):

    def test_mean(self):
        data = [1, 2, 3, 4, 5]
        expected_mean = statistics.mean(data)
        self.assertEqual(mean(data), expected_mean)

if __name__ == '__main__':
    unittest.main()