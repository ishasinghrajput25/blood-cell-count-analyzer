# Input collection and validation module
# Subject: CSE1021 - Introduction to Problem Solving and Programming

"""
VALIDATION MODULE
=================
This module handles all user input operations and robust input validation.
It ensures that:
1. Names and strings are non-empty.
2. Age is a valid positive integer.
3. Gender is chosen from predefined choices.
4. Blood parameters (RBC, WBC, Platelets) are positive numeric values.
5. The application does not crash due to invalid user typing.
"""

def validate_string(prompt, min_len=1):
    """
    Prompts the user for a text input and ensures it is not empty
    or containing only whitespace.
    """
    while True:
        value = input(prompt).strip()
        if len(value) >= min_len:
            return value
        print(">> Error: Input cannot be empty. Please enter a valid text value.")

def validate_positive_float(prompt, param_name="Value"):
    """
    Prompts the user for a positive decimal or whole number.
    Re-prompts until valid input is given.
    Handles:
    - Empty input
    - Non-numeric alphabetic input (ValueError)
    - Zero or negative values
    """
    while True:
        raw_val = input(prompt).strip()
        if not raw_val:
            print(f">> Error: {param_name} cannot be empty. Please enter a number.")
            continue
        try:
            num = float(raw_val)
            if num <= 0:
                print(f">> Error: {param_name} must be greater than zero. Please re-enter.")
                continue
            return num
        except ValueError:
            print(f">> Error: Invalid numerical input '{raw_val}'. Please enter a valid number (e.g. 5.2 or 7500).")

def validate_age():
    """
    Prompts the user for age, ensuring it is a positive integer between 1 and 125.
    """
    while True:
        raw_age = input("Enter Patient Age (in years, 1-125): ").strip()
        if not raw_age:
            print(">> Error: Age cannot be empty.")
            continue
        try:
            age = int(raw_age)
            if 1 <= age <= 125:
                return age
            else:
                print(">> Error: Please enter a realistic age between 1 and 125.")
        except ValueError:
            print(f">> Error: '{raw_age}' is not a valid whole number for age. Please enter an integer.")

def validate_gender():
    """
    Prompts the user to select gender from predefined options.
    Returns normalized string: 'Male', 'Female', or 'Other'.
    """
    print("\nSelect Gender:")
    print("  1. Male")
    print("  2. Female")
    print("  3. Other / Prefer not to specify")
    
    while True:
        choice = input("Enter choice (1-3) or type Male/Female/Other: ").strip().lower()
        if choice in ['1', 'm', 'male']:
            return "Male"
        elif choice in ['2', 'f', 'female']:
            return "Female"
        elif choice in ['3', 'o', 'other']:
            return "Other"
        else:
            print(">> Error: Invalid selection. Please select 1, 2, or 3.")

def get_user_information(sample_counter=1):
    """
    MODULE 1: Collects and validates patient/user demographic information.
    Includes optional sample ID.
    Returns a dictionary of patient details.
    """
    print("\n" + "=" * 50)
    print("          MODULE 1: PATIENT INFORMATION")
    print("=" * 50)
    
    name = validate_string("Enter Patient Full Name: ")
    age = validate_age()
    gender = validate_gender()
    
    default_id = f"SMP-{1000 + sample_counter}"
    sample_id = input(f"Enter Sample/Patient ID [Press Enter for default: {default_id}]: ").strip()
    if not sample_id:
        sample_id = default_id

    patient_info = {
        "sample_id": sample_id,
        "name": name,
        "age": age,
        "gender": gender
    }
    
    print("\nPatient information recorded successfully.")
    return patient_info

def get_blood_values():
    """
    MODULE 2: Collects and validates laboratory blood cell values.
    Returns a dictionary of RBC, WBC, and Platelet measurements.
    """
    print("\n" + "=" * 50)
    print("        MODULE 2: BLOOD TEST DATA ENTRY")
    print("=" * 50)
    print("Please enter the measured laboratory values.")
    print("Note the standard units specified for each parameter.\n")
    
    rbc = validate_positive_float(
        "1. Enter RBC Count (in million cells/mcL, e.g., 4.8): ",
        param_name="RBC count"
    )
    
    wbc = validate_positive_float(
        "2. Enter WBC Count (in cells/mcL, e.g., 7200): ",
        param_name="WBC count"
    )
    
    platelets = validate_positive_float(
        "3. Enter Platelet Count (in cells/mcL, e.g., 250000): ",
        param_name="Platelet count"
    )
    
    blood_values = {
        "RBC": rbc,
        "WBC": wbc,
        "Platelets": platelets
    }
    
    print("\nBlood test values recorded successfully.")
    return blood_values
