# Report formatting and presentation module
# Subject: CSE1021 - Introduction to Problem Solving and Programming

"""
REPORT MODULE
=============
This module formats and presents the blood cell count analysis results.
It builds a clean, readable text report with aligned columns,
displays a quantitative summary, and appends mandatory educational disclaimers.
"""

from reference_ranges import EDUCATIONAL_DISCLAIMER

def format_record_report(record):
    """
    Constructs a comprehensive, nicely-formatted string representation
    of a complete blood test record.
    """
    patient = record["patient_info"]
    analysis = record["analysis"]
    params = analysis["parameters"]
    summary = analysis["summary"]

    lines = []
    lines.append("\n" + "=" * 70)
    lines.append("                  BLOOD CELL COUNT ANALYSIS REPORT")
    lines.append("              Educational Health Informatics Laboratory")
    lines.append("=" * 70)
    lines.append(f"Sample / Patient ID : {patient.get('sample_id', 'N/A')}")
    lines.append(f"Patient Name        : {patient['name']}")
    lines.append(f"Age                 : {patient['age']} years")
    lines.append(f"Gender              : {patient['gender']}")
    lines.append("-" * 70)
    lines.append(f"{'Parameter':<12} | {'Value':<12} | {'Reference Range':<22} | {'Status'}")
    lines.append("-" * 70)

    for p in params:
        val_str = f"{p['value']:.1f}" if p['parameter'] == "RBC" else f"{int(p['value'])}"
        range_display = f"{p['min']}-{p['max']}" if p['parameter'] == "RBC" else f"{int(p['min'])}-{int(p['max'])}"
        lines.append(f"{p['parameter']:<12} | {val_str:<12} | {range_display:<22} | {p['status']}")

    lines.append("-" * 70)
    lines.append("SUMMARY")
    lines.append(f"  Total parameters analyzed : {summary['total_parameters']}")
    lines.append(f"  Within reference range    : {summary['within_range']}")
    lines.append(f"  Below reference range     : {summary['low']}")
    lines.append(f"  Above reference range     : {summary['high']}")
    lines.append("-" * 70)
    
    lines.append("EDUCATIONAL OBSERVATIONS:")
    for p in params:
        lines.append(f"  * {p['parameter']} ({p['description']}): {p['educational_note']}")
        
    lines.append("-" * 70)
    lines.append("IMPORTANT NOTICE:")
    lines.append("This result strictly compares entered numbers against baseline academic")
    lines.append("reference ranges. It DOES NOT indicate, confirm, or rule out any medical")
    lines.append("condition. Please consult a licensed medical doctor for clinical care.")
    lines.append("=" * 70 + "\n")

    return "\n".join(lines)

def display_report(record):
    """
    Prints the formatted record report to the console.
    """
    report_text = format_record_report(record)
    print(report_text)

def display_about():
    """
    Displays background information about the project, course details,
    and developer acknowledgments.
    """
    print("\n" + "=" * 70)
    print("                 ABOUT BLOOD CELL COUNT ANALYZER")
    print("=" * 70)
    print("Course          : CSE1021 - Introduction to Problem Solving and Programming")
    print("Program         : B.Tech Computer Science and Engineering")
    print("Specialization  : Health Informatics")
    print("Purpose         : To computationally analyze and categorize routine blood-cell")
    print("                  counts (RBC, WBC, Platelets) using core programming constructs")
    print("                  such as conditions, loops, functions, lists, and dictionaries.")
    print("-" * 70)
    print("Key Concepts Demonstrated:")
    print("  1. Variables and Data Types (int, float, str, bool, list, dict)")
    print("  2. Structured Input/Output and Exception Handling (try-except)")
    print("  3. Decision Making Statements (if, elif, else)")
    print("  4. Repetition Structures (while loops, for loops)")
    print("  5. Modular Functions with explicit parameters and return values")
    print("  6. Fundamental Algorithms (Comparison, Linear Search, Counting)")
    print("-" * 70)
    print(EDUCATIONAL_DISCLAIMER)
