### 1. `test_summary_stats`

* **The Task:** Calculate the **mean** and **standard deviation** for a list of numerical values.
* **The Concept:** This is the foundation of **Descriptive Statistics**. Before modeling, a data scientist must understand the "center" and the "spread" of the data.
* **Python Skill:** Using `for` loops to accumulate a sum, the `len()` function, and the `math.sqrt()` library.

### 2. `test_five_number_summary`

* **The Task:** From a list of values, identify the Minimum, 25th percentile (), Median (), 75th percentile (), and Maximum.
* **The Concept:** This introduces **Exploratory Data Analysis (EDA)**. The 5-number summary is used to create Box Plots and detect outliers in a dataset.
* **Python Skill:** Sorting lists with `.sort()`, list indexing (accessing specific positions), and finding the middle index.

### 3. `test_batch_min_max_scaler`

* **The Task:** Take a list of raw values and return a *new* list where every value has been scaled between 0 and 1.
* **The Concept:** This scales the **Data Normalization** concept from Lab 2. Instead of scaling one number, you are normalizing an entire feature column to prepare it for a machine learning model.
* **Python Skill:** The **Accumulator Pattern** (creating an empty list and using `.append()` within a loop).

### 4. `test_batch_sentiment_binner`

* **The Task:** Take a list of satisfaction scores and convert them into a list of strings: `"Low"`, `"Medium"`, or `"High"`.
* **The Concept:** This scales **Categorical Binning**. It transforms raw continuous numerical data into searchable, grouped categories.
* **Python Skill:** Nested logic—running an `if-elif-else` structure inside a `for` loop.