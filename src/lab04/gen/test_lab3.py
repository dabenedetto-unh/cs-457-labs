import unittest
import os
import json

from solutions.lab04.gen.lab3 import *

class TestLab3(unittest.TestCase):

    # Test 1: Dictionary Frequency
    def test_frequency_counter(self):
        items = ["Low", "High", "Low", "Medium", "Low"]
        expected = {"Low": 3, "High": 1, "Medium": 1}
        self.assertEqual(frequency_counter(items), expected)

    # Test 2: Mapping Tuples to Dicts
    def test_feature_mapping(self):
        raw = [("Alice", 90, "Pass"), ("Bob", 55, "Fail")]
        expected = [
            {"name": "Alice", "score": 90, "status": "Pass"},
            {"name": "Bob", "score": 55, "status": "Fail"}
        ]
        self.assertEqual(feature_mapping(raw), expected)

    # Test 3: CSV Extraction
    def test_csv_column_extractor(self):
        filename = "test_data.csv"
        with open(filename, "w") as f:
            f.write("id,score,age\n1,85.5,22\n2,90.0,25")
        
        # Extract "score" (index 1)
        result = csv_column_extractor(filename, 1)
        self.assertEqual(result, [85.5, 90.0])
        os.remove(filename)

    # Test 4: JSON Loading
    def test_load_config(self):
        filename = "config.json"
        config_data = {"learning_rate": 0.01, "epochs": 10}
        with open(filename, "w") as f:
            json.dump(config_data, f)
        
        self.assertEqual(load_config(filename), config_data)
        os.remove(filename)

    # Test 5: Report Writing
    def test_write_report(self):
        filename = "report.txt"
        stats = {"Mean": 50.222, "StdDev": 5.1}
        write_report(filename, stats)
        
        with open(filename, "r") as f:
            content = f.read()
            self.assertIn("Mean: 50.22", content)
            self.assertIn("StdDev: 5.10", content)
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()