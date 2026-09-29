# CSE1021 Lab Viva Questions & Answers
**Subject:** CSE1021 – Introduction to Problem Solving and Programming  
**Project:** Blood Cell Count Analyzer  
**Student:** Isha Singh Rajput (First-Year B.Tech CSE – Health Informatics)

---

### Q1: What is the main idea behind your project, and why did you choose it for Health Informatics?
**Answer:**  
In healthcare, a Complete Blood Count (CBC) is almost always the first test ordered when checking a patient's health. But when a patient or non-specialist gets the lab sheet, it is just a confusing table of numbers, decimals, and units like cells/mcL.  
I wanted to build a simple Python program that takes in a patient's numbers, checks that they were entered correctly without crashing, compares them against normal medical reference ranges, and prints out a clean, readable report. It connects our introductory programming course directly to health informatics by showing how basic algorithms can help automate and structure biomedical data.

---

### Q2: Why did you split the code into multiple files instead of writing everything in `main.py`?
**Answer:**  
I used modular programming so that each file has just one clear responsibility:
- `validation.py` only handles taking input and preventing crashes from bad data.
- `analyzer.py` handles the comparison math and counting.
- `reference_ranges.py` keeps all the normal range numbers in one place.
- `records.py` manages session history and search.
- `report.py` formats the output table.
- `main.py` simply coordinates the menu loop.

This made it much easier to debug because if something broke with user input, I knew to check `validation.py`. It also means if reference ranges change in the future, I can update them in `reference_ranges.py` without risking breaking the logic in `analyzer.py`.

---

### Q3: How did you implement input validation, and how do you stop the program from crashing if someone types letters instead of numbers?
**Answer:**  
I used `while True` loops combined with `try-except ValueError` blocks:
- When the user types an input, Python's `input()` returns a string.
- Inside `validate_positive_float()`, I attempt to convert that string using `float(raw_val)` inside a `try` block.
- If the user typed letters (like "ten" or "abc"), Python raises a `ValueError`. My `except ValueError:` block catches it immediately, prints a helpful error message, and the `while` loop restarts without the program crashing.
- If the conversion succeeds, I then check `if num <= 0`. If it's zero or negative, I show an error and prompt again. The loop only exits and returns the number once a valid, positive float is entered.

---

### Q4: Why did you use `if-elif-else` for classification instead of separate `if` statements?
**Answer:**  
A blood count value can only be in one state at any given time—it is either below the minimum range, above the maximum range, or in between.  
Using `if-elif-else` creates mutually exclusive checks:
```python
if value < min_range:
    return "LOW"
elif value > max_range:
    return "HIGH"
else:
    return "WITHIN RANGE"
```
As soon as one condition evaluates to True, Python skips the rest of the checks, which is both faster and avoids accidental logic overlaps. If I used multiple standalone `if` statements, Python would check every condition even after already finding a match.

---

### Q5: How did you handle gender-specific reference ranges for Red Blood Cells?
**Answer:**  
In `reference_ranges.py`, I created a nested dictionary for RBC with separate ranges:
- Male: 4.5 to 5.9 million cells/mcL
- Female: 4.1 to 5.1 million cells/mcL
- Other/General: 4.1 to 5.9 million cells/mcL (as an inclusive baseline)

When the user enters the patient's gender in Module 1, the program validates it. Then, `get_rbc_range(gender)` converts the gender string to lowercase and looks up the corresponding `(min_val, max_val)` tuple from the dictionary.

---

### Q6: What data structures did you use in this project and why?
**Answer:**  
I used three main Python data structures:
1. **Lists (`[]`):**
   - An in-memory list `session_records` to store patient records sequentially as they are entered during the session.
   - Lists of results when looping through parameter dictionaries.
2. **Dictionaries (`{}`):**
   - Perfect for key-value pairs. I used them to store the reference ranges table, patient information (`{"name": ..., "age": ..., "gender": ...}`), and structured test results.
3. **Tuples (`()`):**
   - Used for fixed numerical boundaries, like returning `(min_range, max_range)` from range lookup functions, because reference boundaries should be immutable pairs.

---

### Q7: Explain the counting logic in `analyze_blood_values()`.
**Answer:**  
I used an accumulator counting pattern:
1. First, I initialize three counter variables to zero: `within_range_count = 0`, `low_count = 0`, and `high_count = 0`.
2. I iterate through the list of analyzed parameters using a `for item in results:` loop.
3. For each parameter, I inspect `item["status"]`:
   - If it is `"WITHIN RANGE"`, I increment `within_range_count += 1`.
   - If it is `"LOW"`, I increment `low_count += 1`.
   - If it is `"HIGH"`, I increment `high_count += 1`.
4. Finally, I package the counts along with `total_parameters` into a summary dictionary and return it.

---

### Q8: How does the search function work in `records.py`? What is the algorithm and time complexity?
**Answer:**  
I implemented **Linear Search**:
- For name search, the function iterates through each saved record in `session_records` from start to finish.
- It normalizes both the search query and the stored patient name using `.lower()` and checks `if query in patient_name`.
- Because the list is unordered as records are entered over time, inspecting each record one-by-one is simple and reliable.
- **Time Complexity:** O(n), where n is the number of records saved in the session (checking each record one by one).
- **Space Complexity:** O(m), where m is the number of matching records found.

---

### Q9: Why is this application strictly an educational tool and not a clinical diagnosis system?
**Answer:**  
In healthcare, you cannot diagnose a disease (like anemia or infection) just from an isolated blood cell number. A real doctor looks at a patient's symptoms, medical history, physical exams, and multiple follow-up tests.  
Claiming that a low RBC means "anemia" or a high WBC means "infection" in software would be medically unsafe and ethically irresponsible. My program acts strictly as an educational comparison tool: it compares numbers against normal ranges, reports where they stand, and explicitly advises users to consult a licensed medical doctor.

---

### Q10: How does Python know how to import functions from your other files like `from validation import get_user_information`?
**Answer:**  
When you run `python main.py`, Python automatically adds the folder containing `main.py` to the top of `sys.path` (the list of directories Python searches for modules). When it sees `from validation import get_user_information`, it looks in that same current directory, finds `validation.py`, loads its functions into memory, and lets `main.py` call them.

---

### Q11: What is the difference between mutable and immutable data types in Python? Give examples from your project.
**Answer:**  
- **Mutable types** can be changed after they are created without creating a new object in memory. In my project:
  - The `session_records` list (modified with `.append()`).
  - Dictionaries storing patient data and test results.
- **Immutable types** cannot be modified once created. If you change them, Python creates a new object in memory. In my project:
  - Strings (like patient names and IDs).
  - Integers (like `age`).
  - Floats (like blood values).
  - Tuples (like `(min_val, max_val)` reference ranges).

---

### Q12: What would you improve or add if you had more time to work on this project?
**Answer:**  
1. **Save data to disk:** Right now records are in RAM, so they reset when the program closes. I would like to save them to a local JSON or CSV file.
2. **Add a GUI:** Build a beginner-friendly desktop interface using Python's built-in `tkinter` module.
3. **Include more parameters:** Expand the panel to include Hemoglobin (Hb), Hematocrit (PCV), and differential white cell counts (like Neutrophils and Lymphocytes).
4. **Export PDF Reports:** Add a direct feature to export nicely formatted PDF report cards for patients to download or print.
