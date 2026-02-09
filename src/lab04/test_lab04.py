import unittest

from lab04_dicts import *
from lab04_strings import phone_cleaner_batch, parse_currency_batch

class TestLabFunctions(unittest.TestCase):
    
    def test_phone_cleaner(self):
        '''
        examples:
        >>> phone_cleaner(["555-123-4567", "(555) 123 4567", "555.123.4567"])
        ['5551234567', '5551234567', '5551234567']
        '''


    def test_parse_currency_batch(self):
        '''
        examples:
        >>> parse_currency_batch(["$1,234.56", "$7,890.12"])
        [1234.56, 7890.12]
        '''


if __name__ == '__main__':
    unittest.main()

