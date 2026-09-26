# Project Statement & Scope Specification

## Project Title
**Blood Cell Count Analyzer: An Educational Blood Test Data Analysis System**

**Course**: CSE1021 – Introduction to Problem Solving and Programming  
**Branch & Specialization**: First-Year B.Tech Computer Science and Engineering (Health Informatics)

---

## 1. Problem Statement
In clinical medicine and laboratory health informatics, a Complete Blood Count (CBC) is one of the most frequently ordered diagnostic evaluations. A standard CBC assesses multiple vital cellular components of blood, including Red Blood Cells (RBC), White Blood Cells (WBC), and Platelets.

Manual inspection and interpretation of raw numerical laboratory reports can be time-consuming, prone to human transcription or comparison errors, and difficult for non-specialists to quickly assess. Furthermore, introductory students in health informatics require concrete programming examples that illustrate how computational algorithms can ingest, validate, compare, and categorize physiological data against reference standards.

The problem is to develop a beginner-friendly, modular, console-based Python application that automates the verification and comparison of standard blood cell parameters against academic reference ranges, flags out-of-range deviations, counts summary statistics, and outputs a formatted report without introducing medically speculative diagnostic claims.

---

## 2. Project Scope

### In-Scope:
1. **Interactive Data Capture**:
   - Patient demographic capture: Full Name, Age (positive integer), Gender (Male/Female/Other), and unique Sample/Patient ID.
   - Laboratory measurements capture: RBC (million cells/mcL), WBC (cells/mcL), and Platelet count (cells/mcL).
2. **Robust Input Validation**:
   - Preventing empty, negative, or non-numerical values.
   - Graceful re-prompting using `while` loops and `try-except ValueError` blocks.
3. **Reference Range Engine**:
   - Centralized dictionary lookup for reference ranges.
   - Gender-specific range matching for Red Blood Cell count.
4. **Algorithmic Classification & Counting**:
   - Conditional classification (`if-elif-else`) into `LOW`, `WITHIN RANGE`, or `HIGH`.
   - Counting total parameters, within-range parameters, low parameters, and high parameters.
5. **Report & Observation Formatting**:
   - Generating an aligned tabular report showing parameters, observed values, reference intervals, and status.
   - Appending clear educational observations and non-diagnostic disclaimers.
6. **Session-Level In-Memory Record Management**:
   - Storing completed tests in Python lists of dictionaries.
   - Searching historical session records by patient name or sample ID using linear search.

### Out-of-Scope (Design Constraints):
- **No Clinical Diagnosis or Disease Labeling**: The software does not diagnose conditions such as anemia, leukemia, or thrombocytopenia, adhering strictly to ethical and educational boundaries.
- **No Complex External Frameworks**: No heavy third-party packages, machine learning models, or web frameworks (e.g., Django, Flask, Pandas, TensorFlow) are used, keeping the codebase transparent and aligned with the first-year syllabus.
- **No Persistent External SQL/NoSQL Database**: Storage is kept in memory during runtime to focus on core algorithmic data structures (lists and dictionaries).

---

## 3. Target Users
1. **First-Year Health Informatics & CSE Students**:
   - Learners studying how programming constructs (loops, conditions, functions, and dictionaries) solve health-data problems.
2. **Academic Evaluators and Faculty**:
   - Instructors evaluating problem-solving methodologies, algorithm design, pseudocode-to-code mapping, and code clarity during laboratory vivas.
3. **General Users & Learners**:
   - Individuals seeking to understand how laboratory reference intervals relate to measured physiological metrics.

---

## 4. High-Level Features
- **Menu-Driven Interface**: Six-option interactive console menu running in a resilient execution loop.
- **Demographic & Value Validation**: Prevents invalid types, zero/negative inputs, and missing names.
- **Gender-Sensitive RBC Evaluation**: Accurately selects male or female reference baselines.
- **Linear Search Module**: Rapid session lookup by patient name or unique sample ID.
- **Educational Baseline Display**: Standalone option to inspect active reference ranges.
- **Mandatory Medical Disclaimer**: Prominently presented on reports and information screens.
