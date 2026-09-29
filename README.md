# Blood Cell Count Analyzer
An Educational Blood Test Data Analysis Tool  
**Course:** CSE1021 – Introduction to Problem Solving and Programming  
**Author:** Isha Singh Rajput (First-Year B.Tech CSE – Health Informatics)

---

## About The Project

As a first-year student specializing in Health Informatics, I wanted to build my course project around actual healthcare data rather than solving textbook math problems. In real-world medicine, almost everyone has had a Complete Blood Count (CBC) test done at some point. When patients receive their printed lab sheet, it usually looks like an intimidating grid of decimals, unfamiliar units, and reference numbers. Unless you have medical training, it's difficult to know what the numbers mean or whether a slight difference is something to worry about.

I built the **Blood Cell Count Analyzer** to explore how foundational programming concepts can help organize and interpret this data. The program runs directly in the terminal, guides the user through entering patient information and lab numbers, guards against invalid typing, compares values against standard academic reference ranges, and prints out an aligned, easy-to-read summary table.

### What Parameters Does It Check?
- **Red Blood Cells (RBC):** These carry oxygen from our lungs to the rest of our body. Normal counts differ between biological males and females, so the program takes gender into account.
- **White Blood Cells (WBC):** The body's immune cells that help fight off bacterial and viral infections.
- **Platelets:** Tiny cell fragments that help blood clot when you get injured.

---

## Key Features

- **Menu-Driven Terminal Interface:** Simple 6-option main menu that keeps running in a loop until you choose to exit.
- **Defensive Input Handling:** The program never crashes if you accidentally enter letters, negative numbers, or blank lines. It catches errors with `try-except` blocks and gently asks you to re-type.
- **Gender-Sensitive RBC Ranges:** Automatically chooses the appropriate physiological reference range for Red Blood Cells based on the patient's selected gender.
- **Clean Tabular Reports:** Uses formatted f-strings with column width specifiers so the output looks like a neat, aligned lab report card.
- **In-Memory Session History:** Keeps a running list of all records entered during your session using a Python list of dictionaries.
- **Linear Search:** Look up previous tests by patient name (case-insensitive partial matching, so typing `"rahul"` finds `"Rahul Sharma"`) or by unique Sample ID.
- **Zero Third-Party Packages:** Built entirely with the standard Python library—no `pip install` required. Anyone with Python 3.8+ can clone and run it immediately.
- **Clear Ethical Disclaimers:** Every report reminds users that this tool is strictly educational and not a replacement for a medical doctor.

---

## Topics Covered from CSE1021
This project demonstrates the core programming fundamentals covered in our first-year syllabus:
- **Conditionals (`if-elif-else`)**: For categorizing blood counts into LOW, WITHIN RANGE, or HIGH based on reference ranges.
- **Loops & Exceptions (`while`, `try-except`)**: To catch bad inputs like letters or empty entries so the terminal never crashes.
- **Lists and Dictionaries**: For storing reference ranges and managing session test records in memory.
- **Linear Search**: For finding saved patient records by name (case-insensitive substring match) or sample ID.
- **Functions & Modules**: Splitting code across six Python files for clean organization.

---

## Files in This Repository
- `main.py` - Runs the interactive menu loop and coordinates user actions.
- `validation.py` - Handles safe input prompts for demographics and blood counts.
- `analyzer.py` - Compares blood counts with normal ranges and counts totals.
- `reference_ranges.py` - Central dictionary containing normal reference limits for RBC, WBC, and Platelets.
- `records.py` - Stores session records in memory and performs linear search.
- `report.py` - Formats the tabular report card displayed in the terminal.
- `run_tests.py` - Runs automated test cases covering normal, abnormal, and edge inputs.
- `PROJECT_REPORT.md` / `Project_Report.pdf` - Complete course project report.
- `statement.md` - Problem statement and project scope specification.
- `VIVA_QUESTIONS_AND_ANSWERS.md` - Viva preparation questions and answers.

---

## How to Run

### Requirements
- Python 3.8 or higher installed on your computer.
- No third-party packages need to be installed.

### Quick Start
1. Clone or download this repository:
   ```bash
   git clone https://github.com/ishasinghrajput25/blood-cell-count-analyzer.git
   cd blood-cell-count-analyzer
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Run the automated test suite:
   ```bash
   python run_tests.py
   ```

---

## How to Use the Application

1. Start the program by running `python main.py`.
2. Choose **Option 1 (Enter New Blood Test)**:
   - Enter the patient's full name and age.
   - Select their gender (`1` for Male, `2` for Female, or `3` for Other).
   - Enter a custom sample ID or simply press Enter to accept the automatic ID (like `SMP-1001`).
   - Enter the three measured lab counts (RBC in million cells/mcL, WBC in cells/mcL, Platelets in cells/mcL).
3. The program immediately displays a formatted table showing the entered values, baseline ranges, status flags (`LOW`, `WITHIN RANGE`, `HIGH`), summary counts, and educational notes.
4. Select **Option 2 (View Previous Records)** to inspect all tests saved during your current session.
5. Select **Option 3 (Search Record)** to search for an earlier patient by typing their name or sample ID.
6. Select **Option 4 (View Reference Ranges)** to view the standard educational limits table anytime.
7. Select **Option 5 (About / Disclaimer)** to read the project background and ethical guidelines.
8. Select **Option 6 (Exit)** when you are finished.

---

## Sample Report Output

Here is an example of what the generated report looks like in the terminal:

```text
======================================================================
                  BLOOD CELL COUNT ANALYSIS REPORT
              Educational Health Informatics Laboratory
======================================================================
Sample / Patient ID : SMP-1001
Patient Name        : Rahul Sharma
Age                 : 19 years
Gender              : Male
----------------------------------------------------------------------
Parameter    | Value        | Reference Range        | Status
----------------------------------------------------------------------
RBC          | 4.8          | 4.5-5.9                | WITHIN RANGE
WBC          | 6500         | 4500-11000             | WITHIN RANGE
Platelets    | 220000       | 150000-450000          | WITHIN RANGE
----------------------------------------------------------------------
SUMMARY
  Total parameters analyzed : 3
  Within reference range    : 3
  Below reference range     : 0
  Above reference range     : 0
----------------------------------------------------------------------
EDUCATIONAL OBSERVATIONS:
  * RBC (Red Blood Cells): RBC value is within normal educational limits.
  * WBC (White Blood Cells): WBC value is within normal educational limits.
  * Platelets (Platelet Count): Platelet value is within normal educational limits.
----------------------------------------------------------------------
IMPORTANT NOTICE:
This result strictly compares entered numbers against baseline academic
reference ranges. It DOES NOT indicate, confirm, or rule out any medical
condition. Please consult a licensed medical doctor for clinical care.
======================================================================
```

---

## Automated Verification Tests

I created `run_tests.py` to programmatically verify that all calculations, edge boundaries, and search functions behave as expected without requiring manual terminal typing:

| Test Case | Scenario Tested | Input Values | Expected Output | Status |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | All values normal | RBC: 5.0 (M), WBC: 7000, Plt: 250000 | RBC, WBC, Plt all `WITHIN RANGE` | **PASSED (100%)** |
| **TC-02** | Single value below range | RBC: 3.5 (M), WBC: 6500, Plt: 220000 | RBC flagged as `LOW` | **PASSED (100%)** |
| **TC-03** | Single value above range | RBC: 4.8 (F), WBC: 13500, Plt: 300000 | WBC flagged as `HIGH` | **PASSED (100%)** |
| **TC-04** | Multiple abnormal values | RBC: 3.8 (M), WBC: 14200, Plt: 110000 | RBC `LOW`, WBC `HIGH`, Plt `LOW` | **PASSED (100%)** |
| **TC-05** | Inclusive boundaries & search | Exact cutoffs (4.50, 5.90, 4.49, 5.91) | Exact boundaries stay within range; linear search matches records | **PASSED (100%)** |

---

## Limitations & Things I Want to Add Next

### Current Limitations:
- **Session-only memory:** Records live in RAM while the program runs and reset when you exit.
- **Three core cell types:** Only looks at RBC, WBC, and Platelets rather than an extended complete blood panel with differential counts.

### Future Enhancements:
1. **Save to JSON or CSV:** Allow users to save their session records to a local file so data persists after closing the terminal.
2. **Simple Desktop GUI:** Build a clean graphical interface with Python's built-in `tkinter` library.
3. **Add More Blood Tests:** Expand to include Hemoglobin (Hb), Hematocrit (PCV), and 5-part differential white cell counts (Neutrophils, Lymphocytes, etc.).
4. **Export Directly to PDF:** Add a one-click option to generate a printable PDF report card.
5. **Patient Trend History:** Plot simple charts showing how a patient's counts change over successive visits.

---

## Educational Disclaimer

This software was developed purely as an educational exercise for the first-year university course **CSE1021 – Introduction to Problem Solving and Programming**. It compares numerical inputs against standardized academic baselines and **does not provide medical diagnoses or healthcare advice**. Always consult a qualified medical professional for interpreting actual clinical diagnostic tests.
