# Reference ranges and constants for educational blood cell count analysis
# Subject: CSE1021 - Introduction to Problem Solving and Programming

"""
REFERENCE RANGES MODULE
=======================
This module defines the educational baseline reference ranges for standard
blood cell counts (RBC, WBC, and Platelets).

IMPORTANT DISCLAIMER:
These ranges are intended strictly for educational and classroom demonstration
purposes in CSE1021 (Introduction to Problem Solving and Programming).
Actual clinical laboratory reference ranges vary based on the analyzing
laboratory, instrumentation, patient age, physiological conditions, and sex.
This application does NOT provide medical diagnosis or clinical advice.
"""

# Predefined educational reference ranges stored in a nested Python dictionary
BLOOD_RANGES = {
    "RBC": {
        "unit": "million cells/mcL",
        "description": "Red Blood Cell Count",
        "male": {
            "min": 4.5,
            "max": 5.9
        },
        "female": {
            "min": 4.1,
            "max": 5.1
        },
        "other": {
            "min": 4.1,
            "max": 5.9
        }
    },
    "WBC": {
        "unit": "cells/mcL",
        "description": "White Blood Cell Count",
        "min": 4500.0,
        "max": 11000.0
    },
    "Platelets": {
        "unit": "cells/mcL",
        "description": "Platelet Count",
        "min": 150000.0,
        "max": 450000.0
    }
}

# Standard educational disclaimer text
EDUCATIONAL_DISCLAIMER = """
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
"""

def get_rbc_range(gender):
    """
    Returns the appropriate RBC minimum and maximum values based on gender.
    Gender input is normalized to lowercase string ('male', 'female', or 'other').
    """
    gender_key = gender.strip().lower()
    if gender_key == "male":
        return BLOOD_RANGES["RBC"]["male"]["min"], BLOOD_RANGES["RBC"]["male"]["max"]
    elif gender_key == "female":
        return BLOOD_RANGES["RBC"]["female"]["min"], BLOOD_RANGES["RBC"]["female"]["max"]
    else:
        # Default educational inclusive range for other/unspecified
        return BLOOD_RANGES["RBC"]["other"]["min"], BLOOD_RANGES["RBC"]["other"]["max"]

def get_wbc_range():
    """
    Returns the minimum and maximum reference values for White Blood Cells.
    """
    return BLOOD_RANGES["WBC"]["min"], BLOOD_RANGES["WBC"]["max"]

def get_platelet_range():
    """
    Returns the minimum and maximum reference values for Platelet count.
    """
    return BLOOD_RANGES["Platelets"]["min"], BLOOD_RANGES["Platelets"]["max"]

def display_reference_ranges():
    """
    Displays the educational reference ranges in a formatted table.
    """
    print("\n" + "=" * 65)
    print("       EDUCATIONAL REFERENCE RANGES (STANDARD BASELINES)")
    print("=" * 65)
    print("Note: Values shown are default academic guidelines, not diagnostic rules.")
    print("-" * 65)
    print(f"{'Parameter':<16} | {'Group/Category':<15} | {'Reference Range':<15} | {'Unit'}")
    print("-" * 65)
    print(f"{'RBC':<16} | {'Male':<15} | {BLOOD_RANGES['RBC']['male']['min']} - {BLOOD_RANGES['RBC']['male']['max']:<9} | {BLOOD_RANGES['RBC']['unit']}")
    print(f"{'RBC':<16} | {'Female':<15} | {BLOOD_RANGES['RBC']['female']['min']} - {BLOOD_RANGES['RBC']['female']['max']:<9} | {BLOOD_RANGES['RBC']['unit']}")
    print(f"{'RBC':<16} | {'Other / General':<15} | {BLOOD_RANGES['RBC']['other']['min']} - {BLOOD_RANGES['RBC']['other']['max']:<9} | {BLOOD_RANGES['RBC']['unit']}")
    print(f"{'WBC':<16} | {'All Adults':<15} | {int(BLOOD_RANGES['WBC']['min'])} - {int(BLOOD_RANGES['WBC']['max']):<7} | {BLOOD_RANGES['WBC']['unit']}")
    print(f"{'Platelets':<16} | {'All Adults':<15} | {int(BLOOD_RANGES['Platelets']['min'])} - {int(BLOOD_RANGES['Platelets']['max']):<5} | {BLOOD_RANGES['Platelets']['unit']}")
    print("-" * 65)
    print("Reference ranges can be modified directly in 'reference_ranges.py'.\n")
