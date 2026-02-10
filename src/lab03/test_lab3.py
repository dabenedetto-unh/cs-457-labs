import unittest

try:
    from lab3 import *
except ImportError:
    from .lab3 import *

class TestLab3(unittest.TestCase):
    
    def test_my_sum_positive_numbers(self):
        '''
        example:
        my_sum([1, 2, 3, 4, 5]) should return 15
        '''

    
    def test_mean_basic(self):
        '''
        example:
        mean([1, 2, 3, 4, 5]) should return 3.0
        '''

    
    def test_median_odd_length(self):
        '''
        example:
        median([1, 2, 3, 4, 5]) should return 3
        '''
    
    def test_median_even_length(self):
        '''
        example:
        median([1, 2, 3, 4]) should return 2.5
        '''
    
    def test_median_unsorted_input(self):
        '''
        example:
        median([5, 1, 3, 2, 4]) should return 3
        '''

    
    def test_quartiles_basic(self):
        '''
        example:
        quartiles([1, 2, 3, 4, 5]) should return (1.5, 3, 4.5)
        '''

    
    def test_quartiles_odd_length(self):
        '''
        example:
        quartiles([1, 2, 3, 4, 5, 6, 7]) should return (2.0, 4.0, 6.0)
        '''
    

if __name__ == '__main__':
    unittest.main()