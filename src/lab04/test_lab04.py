import unittest

try: 
    # load from current directory
    from lab04_dicts import *
    from lab04_strings import *
    from lab04_files import *
    filepath = "data/test_data.csv"
except ImportError:
    # load from package (for unittest)
    from .lab04_dicts import *
    from .lab04_strings import *
    from .lab04_files import *
    filepath = "solutions/lab04/data/test_data.csv"

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

    def test_unique(self):
        '''
        example:
        unique(["apple", "banana", "apple", "orange"]) should return ["apple", "banana", "orange"]
        '''

    def test_frequency_counter(self):
        '''
        example:
        frequency_counter(["apple", "banana", "apple", "orange"]) should return {"apple": 2, "banana": 1, "orange": 1}
        '''

    def test_read_csv(self):
        '''
        example:
        read_csv("test_data.csv") should return a list of lists representing the rows in the CSV file.
        '''

    def test_read_csv_dict(self):
        '''
        example:
        read_csv_dict("test_data.csv") should return a list of dictionaries representing the rows in the CSV file, using the first row as keys.
        '''


if __name__ == '__main__':
    unittest.main()

