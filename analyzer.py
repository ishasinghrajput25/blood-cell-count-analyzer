# Blood cell count analysis and classification module
# Subject: CSE1021 - Introduction to Problem Solving and Programming

"""
ANALYZER MODULE
===============
This module implements the core computational logic for comparing blood cell counts
against educational reference ranges.

It demonstrates:
- Conditional structures (if, elif, else)
- Comparison operators (<, >, <=, >=)
- Counting algorithms
- Modular function design
"""

from reference_ranges import get_rbc_range, get_wbc_range, get_platelet_range, BLOOD_RANGES

def classify_value(value, min_range, max_range):
    """
    Compares a numerical value against lower and upper limits.
    Returns:
    - 'LOW' if value < min_range
    - 'HIGH' if value > max_range
    - 'WITHIN RANGE' if min_range <= value <= max_range
    """
    if value < min_range:
        return "LOW"
    elif value > max_range:
        return "HIGH"
    else:
        return "WITHIN RANGE"

def analyze_rbc(rbc_value, gender):
    """
    Analyzes the Red Blood Cell count considering gender-specific reference ranges.
    Returns a dictionary with parameter details, ranges, and status.
    """
    min_val, max_val = get_rbc_range(gender)
    status = classify_value(rbc_value, min_val, max_val)
    unit = BLOOD_RANGES["RBC"]["unit"]
    
    if status == "LOW":
        note = "RBC value is below the selected reference range."
    elif status == "HIGH":
        note = "RBC value is above the selected reference range."
    else:
        note = "RBC value is within normal educational limits."

    return {
        "parameter": "RBC",
        "description": "Red Blood Cells",
        "value": rbc_value,
        "unit": unit,
        "min": min_val,
        "max": max_val,
        "range_str": f"{min_val} - {max_val} {unit}",
        "status": status,
        "educational_note": note
    }

def analyze_wbc(wbc_value):
    """
    Analyzes White Blood Cell count against standard adult reference range.
    Returns a dictionary with parameter details, ranges, and status.
    """
    min_val, max_val = get_wbc_range()
    status = classify_value(wbc_value, min_val, max_val)
    unit = BLOOD_RANGES["WBC"]["unit"]
    
    if status == "LOW":
        note = "WBC value is below the selected reference range."
    elif status == "HIGH":
        note = "WBC value is above the selected reference range."
    else:
        note = "WBC value is within normal educational limits."

    return {
        "parameter": "WBC",
        "description": "White Blood Cells",
        "value": wbc_value,
        "unit": unit,
        "min": min_val,
        "max": max_val,
        "range_str": f"{int(min_val)} - {int(max_val)} {unit}",
        "status": status,
        "educational_note": note
    }

def analyze_platelets(platelet_value):
    """
    Analyzes Platelet count against standard adult reference range.
    Returns a dictionary with parameter details, ranges, and status.
    """
    min_val, max_val = get_platelet_range()
    status = classify_value(platelet_value, min_val, max_val)
    unit = BLOOD_RANGES["Platelets"]["unit"]
    
    if status == "LOW":
        note = "Platelet value is below the selected reference range."
    elif status == "HIGH":
        note = "Platelet value is above the selected reference range."
    else:
        note = "Platelet value is within normal educational limits."

    return {
        "parameter": "Platelets",
        "description": "Platelet Count",
        "value": platelet_value,
        "unit": unit,
        "min": min_val,
        "max": max_val,
        "range_str": f"{int(min_val)} - {int(max_val)} {unit}",
        "status": status,
        "educational_note": note
    }

def analyze_blood_values(blood_values, gender):
    """
    MODULE 3: Complete analysis coordinator.
    Analyzes RBC, WBC, and Platelets, and computes summary counts.
    
    Demonstrates:
    - Counting algorithm
    - Dictionary aggregation
    """
    rbc_result = analyze_rbc(blood_values["RBC"], gender)
    wbc_result = analyze_wbc(blood_values["WBC"])
    platelet_result = analyze_platelets(blood_values["Platelets"])
    
    results_list = [rbc_result, wbc_result, platelet_result]
    
    # Initialize counters (Fundamental algorithm: Counting)
    total_tested = len(results_list)
    within_range_count = 0
    low_count = 0
    high_count = 0
    
    # Iterate and count each category
    for item in results_list:
        if item["status"] == "WITHIN RANGE":
            within_range_count += 1
        elif item["status"] == "LOW":
            low_count += 1
        elif item["status"] == "HIGH":
            high_count += 1

    summary = {
        "total_parameters": total_tested,
        "within_range": within_range_count,
        "low": low_count,
        "high": high_count,
        "outside_range": low_count + high_count
    }

    return {
        "parameters": results_list,
        "summary": summary
    }
