# Project Statement & Scope Specification

## Project Title
**Blood Cell Count Analyzer: An Educational Blood Test Data Analysis System**

**Course**: CSE1021 – Introduction to Problem Solving and Programming  
**Branch & Specialization**: First-Year B.Tech Computer Science and Engineering (Health Informatics)  
**Student**: Isha Singh Rajput  

---

## 1. Problem Statement
Whenever a patient visits a clinic or hospital, one of the first investigations ordered is a Complete Blood Count (CBC). This test looks at the three core cellular elements in blood: Red Blood Cells (RBC), White Blood Cells (WBC), and Platelets.

However, interpreting a lab sheet is often confusing for everyday people. The numbers span completely different scales—RBC is written in small decimals like 4.8 million/mcL, WBC is in thousands, and Platelets are in hundreds of thousands. On top of that, standard reference ranges aren't fixed; they vary depending on biological factors like sex. When people try checking these numbers manually against reference charts, it is easy to misread columns or misplace decimal points.

As a first-year Health Informatics student, I wanted to address this by building a clean, console-based Python tool. The idea is to take a patient's numbers, check them carefully so typos don't crash the script, match them against standard medical reference ranges, flag anything high or low, and display an organized summary report. Most importantly, the tool stays strictly educational and never attempts to give real medical diagnoses.

---

## 2. Project Scope

### What the Project Covers (In-Scope):
1. **Patient Demographic & Lab Entry**:
   - Asks for patient name (ensuring it's not left blank), age (checked between 1 and 125), and biological sex (needed to pick the right RBC reference range).
   - Generates an auto-incrementing ID like `SMP-1001` or lets the user provide their own sample code.
   - Takes input for RBC, WBC, and Platelet levels one by one.
2. **Crash-Proof Input Validation**:
   - Catches letters and symbols when numbers are expected using `try-except ValueError`.
   - Uses `while` loops to keep prompting until the user enters positive, non-zero values.
3. **Reference Range Engine**:
   - Stores standard reference boundaries in a central dictionary in `reference_ranges.py`.
   - Dynamically selects gender-specific boundaries for RBC (Male: 4.5–5.9, Female: 4.1–5.1 million/mcL).
4. **Classification & Summary Counting**:
   - Compares each lab value using `if-elif-else` logic to categorize it as `LOW`, `WITHIN RANGE`, or `HIGH`.
   - Keeps track of counts for normal, low, and high parameters using accumulator variables.
5. **Formatted Console Report & Educational Notes**:
   - Prints an aligned summary table with clear column widths.
   - Attaches educational notes explaining what each flag means, followed by a clear non-diagnostic disclaimer.
6. **In-Memory Session History & Linear Search**:
   - Stores each completed test in a Python list of dictionaries during the session.
   - Implements linear search to let users find past records by patient name (case-insensitive substring match) or sample ID.

### What is Kept Out-of-Scope (Deliberate Design Decisions):
- **No Clinical Diagnosis**: The tool deliberately avoids diagnosing specific illnesses (such as anemia, infections, or thrombocytopenia). Diagnosing requires clinical history, differential counts, and physical exams that software cannot replace.
- **No External Libraries**: I avoided third-party packages like pandas, tabulate, or web frameworks. Everything is built with standard Python 3 to ensure any teacher or classmate can run it directly without running `pip install`.
- **No Heavy Database Engines**: Records are kept in memory using lists of dictionaries. This keeps the focus squarely on our first-year syllabus concepts—loops, data structures, and basic searching algorithms.

---

## 3. Who This Tool Is For
- **Health Informatics & CSE Students**: Classmates who want to see how basic Python constructs—like loops, conditionals, and dictionaries—can be applied to solve biomedical data problems.
- **Faculty & Lab Evaluators**: Teachers assessing my programming fundamentals, problem breakdown, defensive coding habits, and code readability during the CSE1021 lab viva.
- **Curious Users**: Anyone wanting a simple explanation of how their blood test numbers compare to typical educational reference boundaries.

---

## 4. Key Highlights of the Application
- **Easy-to-use 6-option Menu**: Keeps the program running in an interactive loop until the user chooses to exit.
- **Dependable Input Handling**: Won't crash on invalid keystrokes, spaces, or negative numbers.
- **Gender-Aware RBC Ranges**: Correctly distinguishes between male and female biological normal limits.
- **Simple Linear Search**: Finds previous tests in seconds using partial name matches.
- **Always Visible Disclaimers**: Reminds users right on screen that this is a student project, not medical advice.
