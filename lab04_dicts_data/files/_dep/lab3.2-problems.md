## Lab 3.5: String Parsing & Data Cleaning

### 1. `test_phone_cleaner`

* **The Task:** Take a list of phone numbers in various formats (e.g., `"555-123-4567"`, `"(555) 123 4567"`, `"555.123.4567"`) and return a list of strings containing only the digits.
* **The Concept:** **Data Uniformity**. For a database or model to recognize entities, the "noise" (dashes, dots, spaces) must be removed.
* **Python Skill:** Using `.replace()`, `.isdigit()`, or the "Filter Pattern" within a loop.

### 2. `test_email_domain_extractor`

* **The Task:** Given a list of email addresses, return a dictionary where the keys are the domains (e.g., `"gmail.com"`) and the values are the counts of how many users have that domain.
* **The Concept:** **Feature Engineering**. This extracts a high-level category from a specific string to find patterns in user behavior.
* **Python Skill:** String slicing or the `.split('@')` method combined with dictionary frequency counting.

### 3. `test_currency_converter`

* **The Task:** Convert a list of price strings like `["$1,200.50", "$450.00"]` into a list of floats `[1200.5, 450.0]`.
* **The Concept:** **Type Casting**. Raw financial data is almost always stored as strings with symbols ($, ,) that prevent mathematical operations like `test_euclidean_similarity`.
* **Python Skill:** Removing specific characters and using `float()` conversion.