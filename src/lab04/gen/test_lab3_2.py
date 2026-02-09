from solutions.lab04.gen.lab3_2 import *

import unittest

class TestStringParsing(unittest.TestCase):

    def test_phone_cleaner(self):
        raw_phones = ["(555) 123-4567", "555.123.4567", "555 123 4567"]
        expected = ["5551234567", "5551234567", "5551234567"]
        self.assertEqual(phone_cleaner(raw_phones), expected)

    def test_domain_extractor(self):
        emails = ["test@gmail.com", "user@yahoo.com", "admin@gmail.com"]
        expected = {"gmail.com": 2, "yahoo.com": 1}
        self.assertEqual(domain_extractor(emails), expected)

    def test_parse_currency(self):
        prices = ["$1,200.50", "$45.00", "$10,000"]
        expected = [1200.5, 45.0, 10000.0]
        self.assertEqual(parse_currency(prices), expected)

if __name__ == '__main__':
    unittest.main()
