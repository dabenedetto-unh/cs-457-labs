import unittest

from lab2 import euclidean_distance, investment_growth, min_max_scaler, parse_timestamp, sentiment_binner

class TestLab2Problems(unittest.TestCase):

    def test_euclidean_distance(self):
        '''
        Test the euclidean_distance function with known points.
        The distance between (0, 0) and (3, 4) should be 5.0.
        '''



    def test_investment_growth(self):
        '''
        Test the investment_growth function with known parameters.
        For P=1000, r=0.05, n=12, t=5, the future value should be approximately 1283.36.
        '''



    def test_min_max_scaler(self):
        '''
        Test the min_max_scaler function with a known value and range.
        Scaling 50 in the range 0 to 100 should yield 0.5.
        '''


    def test_timestamp_parser(self):
        '''
        Test the parse_timestamp function with a known number of seconds.
        100000 seconds should convert to 1 day, 3 hours, and 46 minutes.
        '''

    def test_sentiment_binner(self):
        '''
        Test the sentiment_binner function with known satisfaction ratings and transaction sizes.
        A rating of 2 and transaction size of 500 should yield a priority score of 1 (High Priority).
        A rating of 3.5 and transaction size of 200 should yield a priority score of 2 (Medium Priority).
        A rating of 4.5 and transaction size of 50 should yield a priority score of 3 (Low Priority).
        '''


if __name__ == "__main__":
    unittest.main()