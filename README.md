# Blood Cell Count Analyzer
### An Educational Blood Test Data Analysis System

> **Course:** CSE1021 – Introduction to Problem Solving and Programming  
> **Degree Program:** B.Tech Computer Science and Engineering (Specialization in Health Informatics)  
> **Semester:** First Year

---

## 1. Project Title
**Blood Cell Count Analyzer: An Educational Blood Test Data Analysis System**

---

## 2. Project Overview
The **Blood Cell Count Analyzer** is a console-based educational Python application designed to assist students and general users in understanding how fundamental physiological laboratory data can be analyzed computationally. 

The software collects basic complete blood count parameters—specifically **Red Blood Cell (RBC) count**, **White Blood Cell (WBC) count**, and **Platelet count**—validates the entered numbers, compares each measurement against customizable educational reference ranges (including gender-differentiated intervals for RBC), classifies each value as `LOW`, `WITHIN RANGE`, or `HIGH`, and compiles an easy-to-read tabular report with summary counts and educational notes.

---

## 3. Problem Statement
Routine health examinations frequently require interpreting laboratory blood test reports. For individuals without formal medical training or beginning health informatics students, raw laboratory values can appear confusing. Moreover, manual comparison against varying standard intervals is prone to human error.

This project addresses the need for an accessible, beginner-friendly computational tool that demonstrates:
1. How raw patient demographic and biomedical data can be captured and validated.
2. How rule-based conditional algorithms can compare and categorize health data.
3. How results can be organized and presented clearly without making speculative or dangerous medical diagnoses.

---

## 4. Objectives
- **Demonstrate Core Problem-Solving Concepts**: Apply first-year programming concepts such as control flow (`if/elif/else`), loops (`while`, `for`), modular functions, lists, and dictionaries.
- **Implement Robust Input Validation**: Ensure the software handles invalid user input (e.g., negative numbers, letters in numerical fields, empty names) gracefully without crashing.
- **Provide Centralized Reference Ranges**: Store academic reference values in an organized dictionary structure that can be easily modified in a single location.
- **Classify and Quantify Blood Parameters**: Compare inputs with baseline reference boundaries and calculate summary statistics (total analyzed, within range, low, high).
- **Maintain Session History**: Store multiple test records in-memory during a session and provide linear search functionality by patient name or sample ID.
- **Enforce Medical Safety**: Prominently display educational disclaimers and avoid disease diagnostic claims.

---

## 5. Target Users
- **First-Year Engineering Students (CSE / Health Informatics)**: To study practical implementations of introductory Python programming topics.
- **Academic Evaluators and Faculty**: To evaluate the student's mastery of algorithm design, pseudocode mapping, and modular coding.
- **General Learners**: Anyone interested in understanding how blood count values compare against baseline physiological benchmarks.

---

## 6. Features
- **Interactive Menu-Driven Navigation**: Easy-to-use menu with 6 operations running in an continuous loop.
- **Patient Demographic Capture**: Secure collection of Name, Age, Gender, and customizable Sample ID.
- **Strict Input Validation**: Reprompts user automatically on non-numeric, zero, negative, or blank inputs.
- **Gender-Aware RBC Evaluation**: Automatically applies male, female, or general reference ranges for RBC count.
- **Detailed Formatted Tabular Report**: Displays parameter name, entered value, reference range, and status in aligned columns.
- **Summary Statistics**: Computes counts of parameters that are normal, low, and high.
- **Session Records Management**: View all saved records or perform linear search by Patient Name or Sample ID.
- **Educational Reference Range Inspection**: Dedicated menu option to inspect standard baseline values.
- **Strict Educational Disclaimers**: Disclaimers included on startup, about screen, and within every printed report.

---

## 7. Functional Requirements
1. **User Information Module (Module 1)**:
   - Must capture Patient Name (non-empty string).
   - Must capture Patient Age (positive integer, 1–125).
   - Must capture Patient Gender from options (Male, Female, Other).
   - Must assign or accept an optional Sample ID.
2. **Blood Test Data Entry Module (Module 2)**:
   - Must collect RBC (million cells/mcL), WBC (cells/mcL), and Platelet count (cells/mcL).
   - Must validate that all laboratory numbers are positive floats/integers.
3. **Blood Value Analysis Module (Module 3)**:
   - Must fetch reference ranges from `reference_ranges.py`.
   - Must classify values using standard conditionals (`< min`: LOW, `> max`: HIGH, otherwise: WITHIN RANGE).
   - Must aggregate total parameters, count within range, count low, and count high.
4. **Report Generation Module (Module 4)**:
   - Must print a formatted summary table.
   - Must output educational notes per parameter.
   - Must include the non-diagnostic disclaimer.
5. **Storage and Search Module (Module 5)**:
   - Must append records to a list of dictionaries.
   - Must allow viewing all session records in a summary table.
   - Must support searching by patient name or sample ID.

---

## 8. Non-Functional Requirements
- **Usability**: Intuitive command-line prompts with examples (e.g., `e.g., 4.8` or `e.g., 7200`).
- **Reliability & Crash Resilience**: Uncaught exceptions are prevented using `try-except` blocks and input verification loops.
- **Maintainability**: Clear separation of concerns across 5 modular Python files; reference ranges are stored in one central dictionary.
- **Performance**: Instantaneous computation and linear search execution suitable for local workstation use.
- **Resource Efficiency**: Zero heavy dependencies; minimal RAM and CPU utilization.

---

## 9. Technologies Used
- **Language**: Python 3 (Tested on Python 3.8 to 3.14+)
- **Libraries**: Python Standard Library only (`sys`, built-ins)
- **Environment**: Cross-platform (Windows, macOS, Linux)
- **Version Control**: Git / GitHub ready

---

## 10. Python Concepts Used (CSE1021 Syllabus Mapping)
| Concept | Application in Project |
| :--- | :--- |
| **Variables & Types** | Storing integers (`age`), floats (`rbc`, `wbc`), strings (`name`, `sample_id`), and booleans |
| **Input / Output** | Formatted string output with `f-strings`, column alignment with width specifiers (`<12`, `<22`), `input()` |
| **Control Flow (if-elif-else)** | Numerical range comparisons in `classify_value()` and menu branching |
| **Loops (while, for)** | Continuous menu execution (`while True`), input validation retry loops, iteration through parameter lists |
| **Functions & Modularization** | Dedicated single-responsibility functions with defined parameters and return values |
| **Exception Handling (try-except)** | Catching `ValueError` during integer/float casting and preventing program crashes |
| **Lists** | In-memory storage of session records (`session_records`) and parameter analysis results |
| **Dictionaries** | Nested reference ranges (`BLOOD_RANGES`) and structured record objects (`record = {"patient_info": ...}`) |
| **Algorithms** | Linear search (`search_by_name`, `search_by_sample_id`) and counting accumulator logic |

---

## 11. Project Structure
```text
Blood_Cell_Count_Analyzer/
│
├── main.py               # Main program entrypoint and interactive menu loop
├── analyzer.py           # Classification logic, analysis coordinator, and counters
├── validation.py         # Robust input handling, validation loops, and data entry
├── records.py            # In-memory record storage, viewing, and linear search
├── reference_ranges.py   # Centralized reference ranges dictionary and disclaimer
├── report.py             # Tabular report builder, summary display, and about screen
├── run_tests.py          # Automated verification test suite for the 5 required test cases
├── statement.md          # Formal problem statement and academic scope document
├── requirements.txt      # Runtime dependencies specification (Standard library)
└── README.md             # Complete project documentation and guide
```

---

## 12. How to Install
1. **Verify Python Installation**:
   Ensure Python 3.8 or higher is installed on your computer. Open a terminal or Command Prompt and run:
   ```bash
   python --version
   ```
2. **Clone or Download the Project**:
   ```bash
   git clone https://github.com/ishasinghrajput25/blood-cell-count-analyzer.git
   cd blood-cell-count-analyzer
   ```
3. **No External Packages Required**:
   Since the application utilizes only Python built-in features, no `pip install` steps are required.

---

## 13. How to Run
Run the main application by executing:
```bash
python main.py
```

To run the automated verification test suite:
```bash
python run_tests.py
```

---

## 14. How to Use
1. Launch `python main.py`.
2. Select **Option 1 (Enter New Blood Test)**:
   - Enter patient name, age, and select gender (1 for Male, 2 for Female, 3 for Other).
   - Enter optional Sample ID (or press Enter for automatic numbering).
   - Enter RBC count in million cells/mcL (e.g., `4.8`).
   - Enter WBC count in cells/mcL (e.g., `6500`).
   - Enter Platelet count in cells/mcL (e.g., `220000`).
3. View the generated report with column alignments, status classifications, summary counts, and notes.
4. Select **Option 2 (View Previous Records)** to inspect all tests saved in the current session.
5. Select **Option 3 (Search Record)** to search past entries by patient name or sample ID.
6. Select **Option 4 (View Reference Ranges)** to view the educational baseline table.
7. Select **Option 5 (About / Disclaimer)** to read course information and ethical guidelines.
8. Select **Option 6 (Exit)** to terminate the program safely.

---

## 15. Sample Input
```text
Patient Full Name  : Priya Sharma
Patient Age        : 20
Gender Choice      : 2 (Female)
Sample ID          : SMP-2001
RBC Count          : 3.8
WBC Count          : 12500
Platelet Count     : 240000
```

---

## 16. Sample Output
```text
======================================================================
                  BLOOD CELL COUNT ANALYSIS REPORT
              Educational Health Informatics Laboratory
======================================================================
Sample / Patient ID : SMP-2001
Patient Name        : Priya Sharma
Age                 : 20 years
Gender              : Female
----------------------------------------------------------------------
Parameter    | Value        | Reference Range        | Status
----------------------------------------------------------------------
RBC          | 3.8          | 4.1-5.1                | LOW
WBC          | 12500        | 4500-11000             | HIGH
Platelets    | 240000       | 150000-450000          | WITHIN RANGE
----------------------------------------------------------------------
SUMMARY
  Total parameters analyzed : 3
  Within reference range    : 1
  Below reference range     : 1
  Above reference range     : 1
----------------------------------------------------------------------
EDUCATIONAL OBSERVATIONS:
  * RBC (Red Blood Cells): RBC value is below the selected reference range.
  * WBC (White Blood Cells): WBC value is above the selected reference range.
  * Platelets (Platelet Count): Platelet value is within normal educational limits.
----------------------------------------------------------------------
IMPORTANT NOTICE:
This result strictly compares entered numbers against baseline academic
reference ranges. It DOES NOT indicate, confirm, or rule out any medical
condition. Please consult a licensed medical doctor for clinical care.
======================================================================
```

---

## 17. Testing
The application has been verified against 5 standard test cases using the automated verification suite `run_tests.py`:

| Test Case | Inputs Tested | Expected Outcome | Actual Outcome | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Test Case 1: All Within Range** | RBC: 5.0 (M), WBC: 7000, Plt: 250000 | RBC, WBC, Plt = `WITHIN RANGE`<br>Within: 3, Low: 0, High: 0 | Within: 3, Low: 0, High: 0 | **PASSED** |
| **Test Case 2: One Value Below Range** | RBC: 3.5 (M), WBC: 6500, Plt: 220000 | RBC = `LOW`, Others = `WITHIN RANGE`<br>Within: 2, Low: 1, High: 0 | Within: 2, Low: 1, High: 0 | **PASSED** |
| **Test Case 3: One Value Above Range** | RBC: 4.8 (F), WBC: 13500, Plt: 300000 | WBC = `HIGH`, Others = `WITHIN RANGE`<br>Within: 2, Low: 0, High: 1 | Within: 2, Low: 0, High: 1 | **PASSED** |
| **Test Case 4: Multiple Abnormal Values** | RBC: 3.8 (M), WBC: 14200, Plt: 110000 | RBC = `LOW`, WBC = `HIGH`, Plt = `LOW`<br>Within: 0, Low: 2, High: 1 | Within: 0, Low: 2, High: 1 | **PASSED** |
| **Test Case 5: Input & Boundary Checks** | Boundary values (4.5, 5.9), negative & text input handling | Exact boundary values recognized as `WITHIN RANGE`; invalid inputs safely re-prompted | Error caught; search logic verified | **PASSED** |

---

## 18. Limitations
1. **Volatile Memory**: Records are stored in RAM during the active session and will be cleared when the program terminates.
2. **Fixed Parameter Scope**: Evaluates only three primary cellular parameters (RBC, WBC, Platelets) rather than a complete 20+ parameter hematology differential (such as MCV, MCH, Neutrophils, Lymphocytes).
3. **Educational Standard Intervals**: Reference ranges are generalized pedagogical baselines and do not dynamically adjust for high altitudes, pregnancy, pediatrics, or specific clinical lab assay kits.

---

## 19. Future Enhancements
- **Persistent Data Storage**: Add lightweight file persistence using JSON or CSV files without complex databases.
- **Export to PDF/Text File**: Provide an option to save generated reports into downloadable `.txt` or `.pdf` files.
- **Additional Parameters**: Extend the dictionary to include Hemoglobin (Hb), Hematocrit (PCV), and Mean Corpuscular Volume (MCV).
- **Graphical User Interface (GUI)**: Implement a lightweight `tkinter` desktop GUI for visual data entry.
- **Trend Analysis**: Graph changes in blood parameters over time for a patient across multiple visits.

---

## 20. Disclaimer
```text
================================================================================
                           EDUCATIONAL DISCLAIMER
================================================================================
This application is developed for educational purposes only as part of the
course CSE1021 - Introduction to Problem Solving and Programming.

It DOES NOT provide medical diagnosis, treatment recommendations, or clinical
advice. Reference ranges vary across clinical laboratories, geographic regions,
instruments, age groups, and sexes. 

An abnormal parameter in this educational tool does NOT mean the user has a
disease. Always consult a qualified medical professional or registered clinical
laboratory for interpretation of actual diagnostic test results.
================================================================================
```
