## Lab 3: Data Organization and Persistence

### 1. `test_frequency_counter`

* **The Task:** Take a list of categories (e.g., product types or sentiment labels) and return a **dictionary** where keys are the labels and values are the counts of how often they appear.
* **The Concept:** **Categorical Profiling**. Before visualizing data, you must aggregate it. This is the manual version of a "Value Counts" operation in libraries like Pandas.
* **Python Skill:** Initializing a dictionary, checking for key existence (`if key in dict:`), and incrementing values.

### 2. `test_feature_dictionary_mapping`

* **The Task:** Given a list of "Student" or "User" tuples—e.g., `("Alice", 85, "Pass")`—convert them into a list of dictionaries with descriptive keys: `{"name": "Alice", "score": 85, "status": "Pass"}`.
* **The Concept:** **Data Structuring**. In real-world pipelines, data is often ingested as raw rows (tuples) and needs to be mapped to JSON-like objects for readability and API consumption.
* **Python Skill:** Dictionary literal construction and list comprehension (or the accumulator pattern).

### 3. `test_csv_column_extractor`

* **The Task:** Read a small `.csv` file (using the standard `open()` and `split(',')` methods) and extract a single column of numerical data into a Python list.
* **The Concept:** **Data Ingestion**. This is the "Hello World" of File I/O. It bridges the gap between a file on a hard drive and a list in Python memory.
* **Python Skill:** Using `with open(...) as f:`, `.strip()`, `.split()`, and skipping the header row.

### 4. `test_json_config_parser`

* **The Task:** Read a `.json` configuration file containing model parameters (e.g., `{"learning_rate": 0.01, "epochs": 50}`) and return the dictionary.
* **The Concept:** **Metadata Management**. Data scientists use config files to track experiment parameters so they don't have to hard-code values into their scripts.
* **Python Skill:** `import json` and `json.load()`.

### 5. `test_summary_report_writer`

* **The Task:** Take the results from your `test_summary_stats` (Mean, Std Dev) and write them into a nicely formatted `.txt` report or a new `.csv` file.
* **The Concept:** **Reporting & Persistence**. After performing an analysis, the results must be saved so they can be shared with stakeholders without re-running the entire computation.
* **Python Skill:** Writing to files (`mode='w'`), string formatting (f-strings), and newline characters (`\n`).