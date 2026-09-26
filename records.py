# In-memory record management and search module
# Subject: CSE1021 - Introduction to Problem Solving and Programming

"""
RECORDS MODULE
==============
This module manages test records during the active program session.
It uses elementary Python data structures:
- A Python list (`records_list`) to store all session records.
- Dictionaries to represent individual test records.

Demonstrates:
- List operations (append, iteration, indexing)
- Linear search algorithms (searching by Name and by Sample ID)
- Data aggregation and presentation
"""

from report import display_report

def save_record(record, records_list):
    """
    Appends a completed analysis record to the session records list.
    """
    records_list.append(record)
    print(f"\n>> Success: Record for '{record['patient_info']['name']}' saved successfully.")
    print(f">> Total records currently stored in session: {len(records_list)}")

def view_all_records(records_list):
    """
    Displays a table summary of all records stored during the current session.
    Allows user to select a record to view full details.
    """
    print("\n" + "=" * 70)
    print("                  PREVIOUS TEST RECORDS (SESSION)")
    print("=" * 70)
    
    if not records_list:
        print("No test records found in this session.")
        print("Tip: Select '1. Enter New Blood Test' from the main menu to add records.")
        return

    print(f"{'No.':<4} | {'Sample ID':<12} | {'Patient Name':<18} | {'Age/Sex':<10} | {'Status Summary'}")
    print("-" * 70)
    
    for idx, rec in enumerate(records_list, start=1):
        pat = rec["patient_info"]
        summary = rec["analysis"]["summary"]
        age_sex = f"{pat['age']}/{pat['gender'][0]}"
        status_info = f"{summary['within_range']} Normal, {summary['low']} Low, {summary['high']} High"
        print(f"{idx:<4} | {pat['sample_id']:<12} | {pat['name']:<18} | {age_sex:<10} | {status_info}")

    print("-" * 70)
    
    # Optional prompt to view full report of any listed record
    choice = input("\nEnter Record Number to view detailed report (or press Enter to return): ").strip()
    if choice:
        try:
            sel_idx = int(choice)
            if 1 <= sel_idx <= len(records_list):
                selected_record = records_list[sel_idx - 1]
                display_report(selected_record)
            else:
                print(f">> Notice: Number out of range. Expected between 1 and {len(records_list)}.")
        except ValueError:
            print(">> Notice: Invalid entry. Returning to menu.")

def search_by_name(records_list, target_name):
    """
    Linear search algorithm to find records matching a given name.
    Case-insensitive substring search for user convenience.
    """
    matches = []
    target = target_name.strip().lower()
    for rec in records_list:
        patient_name = rec["patient_info"]["name"].lower()
        if target in patient_name:
            matches.append(rec)
    return matches

def search_by_sample_id(records_list, target_id):
    """
    Linear search algorithm to find a record by exact or partial Sample ID.
    """
    matches = []
    target = target_id.strip().lower()
    for rec in records_list:
        sample_id = rec["patient_info"]["sample_id"].lower()
        if target in sample_id:
            matches.append(rec)
    return matches

def search_records_interactive(records_list):
    """
    Interactive search submenu enabling the user to search by Name or Sample ID.
    """
    print("\n" + "=" * 50)
    print("             SEARCH TEST RECORDS")
    print("=" * 50)
    
    if not records_list:
        print("No test records stored in the session to search.")
        return

    print("1. Search by Patient Name")
    print("2. Search by Sample / Patient ID")
    print("3. Return to Main Menu")
    
    choice = input("Enter choice (1-3): ").strip()
    
    if choice == '1':
        query = input("Enter patient name to search: ").strip()
        if not query:
            print(">> Search query cannot be empty.")
            return
        results = search_by_name(records_list, query)
        display_search_results(results, f"name matching '{query}'")
        
    elif choice == '2':
        query = input("Enter Sample ID to search: ").strip()
        if not query:
            print(">> Search query cannot be empty.")
            return
        results = search_by_sample_id(records_list, query)
        display_search_results(results, f"Sample ID matching '{query}'")
        
    elif choice == '3':
        return
    else:
        print(">> Error: Invalid selection. Returning to main menu.")

def display_search_results(results, query_desc):
    """
    Helper function to display records matching a search query.
    """
    if not results:
        print(f"\n>> No matching records found for {query_desc}.")
        return
        
    print(f"\nFound {len(results)} matching record(s):")
    for idx, rec in enumerate(results, start=1):
        print(f"\n--- Result {idx} of {len(results)} ---")
        display_report(rec)
