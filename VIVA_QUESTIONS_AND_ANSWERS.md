# CSE1021 Lab Viva Questions & Model Answers

**Subject:** CSE1021 – Introduction to Problem Solving and Programming  
**Project:** Blood Cell Count Analyzer (Health Informatics)

---

### Q1: What is the main objective of this project, and why is it relevant to your specialization?
**Answer:**  
The objective of this project is to develop a modular, beginner-friendly computational tool that captures basic blood cell parameters (RBC, WBC, and Platelets), validates them, compares them against predefined academic reference intervals, categorizes them as Low, Normal, or High, and generates a formatted report.  
As a Health Informatics student, this demonstrates the foundation of clinical decision support systems (CDSS) and laboratory information systems (LIS): how computational logic can systematically structure, validate, and interpret biomedical data to reduce manual comparison errors.

---

### Q2: Why did you divide the program into multiple Python files instead of writing everything in a single file?
**Answer:**  
We used modular programming principles:
1. **Separation of Concerns:** Each module has a single clear responsibility (e.g., `validation.py` handles input sanitization, `analyzer.py` handles logic and classification, `reference_ranges.py` holds data thresholds, `report.py` formats output, and `records.py` manages storage).
2. **Maintainability:** If reference ranges change, we only modify `reference_ranges.py` without touching the analysis logic.
3. **Reusability and Readability:** Functions can be imported and tested independently (as demonstrated in `run_tests.py`).

---

### Q3: How did you implement input validation, and how does your program prevent crashing when a user enters alphabets or negative numbers?
**Answer:**  
We implemented input validation using infinite `while True` loops combined with Python's `try-except ValueError` blocks and conditional boundary checks:
- When reading numerical inputs like RBC, `input()` returns a string.
- In `validate_positive_float()`, we use `float(raw_val)` inside a `try` block. If the user enters letters (e.g., "abc"), Python raises a `ValueError`, which our `except` block catches, displaying a friendly error message and looping back.
- If the cast succeeds, we check `if num <= 0`. If true, an error is printed, and the loop repeats.
- Only when a positive number is supplied does the function `return num`, terminating the validation loop.

---

### Q4: Explain the difference between `if-elif-else` and multiple standalone `if` statements. Which one did you use for classification?
**Answer:**  
- **`if-elif-else`** creates mutually exclusive decision paths. As soon as one condition evaluates to `True`, the corresponding block executes, and all remaining conditions are skipped.
- **Multiple `if` statements** evaluate every single condition independently, even if an earlier condition was satisfied.  
In our `classify_value()` function:
```python
if value < min_range:
    return "LOW"
elif value > max_range:
    return "HIGH"
else:
    return "WITHIN RANGE"
```
A blood count value cannot be simultaneously below the minimum and above the maximum. Using `if-elif-else` is both semantically correct and computationally efficient.

---

### Q5: How did you handle gender-specific reference ranges for Red Blood Cells?
**Answer:**  
In `reference_ranges.py`, the `BLOOD_RANGES` dictionary stores separate sub-dictionaries for male and female RBC baselines:
- Male: 4.5 – 5.9 million cells/mcL
- Female: 4.1 – 5.1 million cells/mcL
- Other/General: 4.1 – 5.9 million cells/mcL (an inclusive academic fallback)  
The function `get_rbc_range(gender)` accepts the validated patient gender, normalizes the string with `.strip().lower()`, and returns the matching `(min, max)` tuple.

---

### Q6: What data structures did you use in this project, and why?
**Answer:**  
We used:
1. **Lists (`[]`):**
   - An in-memory list `session_records = []` to store sequential test records throughout the session.
   - Lists of parameter dictionaries to iterate through for analysis and printing.
2. **Dictionaries (`{}`):**
   - Used for key-value pair associations.
   - Storing nested reference ranges (`BLOOD_RANGES`).
   - Storing patient information (`{"name": ..., "age": ..., "gender": ...}`).
   - Storing structured results for each parameter.
3. **Tuples (`()`):**
   - Returned by range helper functions (e.g., `return min_val, max_val`) because the bounds are a fixed pair of values.

---

### Q7: Explain the counting algorithm used in `analyze_blood_values()`.
**Answer:**  
The counting algorithm follows these steps:
1. Initialize accumulator variables to zero: `within_range_count = 0`, `low_count = 0`, `high_count = 0`.
2. Iterate through the results list using a `for item in results_list:` loop.
3. Inspect `item["status"]` with an `if-elif-else` condition:
   - If `"WITHIN RANGE"`, increment `within_range_count += 1`.
   - If `"LOW"`, increment `low_count += 1`.
   - If `"HIGH"`, increment `high_count += 1`.
4. Package the counts into a summary dictionary.

---

### Q8: How does the search feature work in `records.py`? What is the algorithm and time complexity?
**Answer:**  
We implemented **Linear Search**:
- In `search_by_name()`, we iterate through each record in `records_list` sequentially.
- We extract `record["patient_info"]["name"].lower()` and check if `target in patient_name`.
- Because the list is unordered, linear search inspects each element one by one.
- **Time Complexity:** $O(N)$ where $N$ is the number of records in the session.
- **Space Complexity:** $O(M)$ where $M$ is the number of matching records found.

---

### Q9: Why is this application not a medical diagnostic tool?
**Answer:**  
In medical informatics, diagnostic evaluation requires comprehensive clinical context—including medical history, physical exams, differential counts, symptoms, and confirmation by repeated calibrated assays.  
Presenting an isolated low or high value as a "disease" (e.g., diagnosing anemia or infection) is medically incorrect and unsafe. Our program strictly acts as an educational comparator: it reports whether numbers fall inside or outside defined pedagogical boundaries and explicitly prompts the user to seek licensed medical consultation.

---

### Q10: How does Python import modules from the same folder?
**Answer:**  
When Python executes `main.py`, it automatically places the directory containing `main.py` at the head of `sys.path`. When statements like `from validation import get_user_information` are executed, Python searches the local directory, finds `validation.py`, loads its definitions, and makes the specified function available in `main.py`.

---

### Q11: What are mutable vs. immutable objects in Python? Can you give examples from your project?
**Answer:**  
- **Mutable objects** can have their contents altered after creation without changing their memory ID. Examples in our project: `session_records` (list) using `.append()`, and record dictionaries (`dict`).
- **Immutable objects** cannot be modified after creation. Examples in our project: strings (`str` like patient names), integers (`int` like age), floats (`float` like blood values), and tuples (`(min, max)` ranges).

---

### Q12: How would you extend this project if you had more time?
**Answer:**  
1. Save records permanently to a JSON or CSV file so data persists after closing the terminal.
2. Add a GUI using Python's built-in `tkinter` library.
3. Expand parameters to include Hemoglobin (Hb), Hematocrit (PCV), and complete differential leukocyte counts (Neutrophils, Lymphocytes).
4. Add automated generation of downloadable PDF/text reports.
