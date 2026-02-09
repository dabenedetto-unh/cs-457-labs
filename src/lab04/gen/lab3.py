import json
import os

# 1. Frequency Counter
def frequency_counter(categories):
    counts = {}
    for item in categories:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

# 2. Feature Dictionary Mapping
def feature_mapping(data_tuples):
    structured_data = []
    for name, score, status in data_tuples:
        entry = {"name": name, "score": score, "status": status}
        structured_data.append(entry)
    return structured_data

# 3. CSV Column Extractor
def csv_column_extractor(filepath, col_index):
    data = []
    with open(filepath, 'r') as f:
        next(f) # Skip header
        for line in f:
            parts = line.strip().split(',')
            data.append(float(parts[col_index]))
    return data

# 4. JSON Config Parser
def load_config(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

# 5. Summary Report Writer
def write_report(filepath, stats_dict):
    with open(filepath, 'w') as f:
        f.write("DATA SCIENCE SUMMARY REPORT\n")
        f.write("-" * 27 + "\n")
        for key, value in stats_dict.items():
            f.write(f"{key}: {value:.2f}\n")