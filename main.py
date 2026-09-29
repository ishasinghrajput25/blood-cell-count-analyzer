# main.py
# Main entrypoint and console menu controller
# Course: CSE1021 - Introduction to Problem Solving and Programming
# Author: Isha Singh Rajput

import sys
from reference_ranges import display_reference_ranges, EDUCATIONAL_DISCLAIMER
from validation import get_user_information, get_blood_values
from analyzer import analyze_blood_values
from report import display_report, display_about
from records import save_record, view_all_records, search_records_interactive

def display_menu():
    """
    Prints the 6-option main menu to the terminal.
    """
    print("\n" + "=" * 50)
    print("           BLOOD CELL COUNT ANALYZER")
    print("   Educational Health Informatics Analysis System")
    print("=" * 50)
    print("1. Enter New Blood Test")
    print("2. View Previous Records")
    print("3. Search Record")
    print("4. View Reference Ranges")
    print("5. About / Disclaimer")
    print("6. Exit")
    print("=" * 50)

def handle_new_blood_test(session_records, sample_counter):
    """
    Handles the full workflow for adding a new test:
    takes user demographics and blood values, analyzes them, prints the report,
    and appends the record into session history.
    """
    # Step 1: Collect patient details
    patient_info = get_user_information(sample_counter)
    
    # Step 2: Collect blood cell measurements
    blood_values = get_blood_values()
    
    # Step 3: Analyze values against educational reference ranges
    analysis_result = analyze_blood_values(blood_values, patient_info["gender"])
    
    # Step 4: Assemble the complete record dictionary
    record = {
        "patient_info": patient_info,
        "blood_values": blood_values,
        "analysis": analysis_result
    }
    
    # Step 5: Display report
    display_report(record)
    
    # Step 6: Save record in session list
    save_record(record, session_records)

def main():
    """
    Main application loop.
    Controls execution flow, handles menu selection, and prevents crashes.
    """
    # In-memory storage list for session records
    session_records = []
    sample_counter = 1
    
    # Display welcoming message and brief disclaimer on startup
    print("\nWelcome to the Blood Cell Count Analyzer!")
    print("Designed for CSE1021 - Introduction to Problem Solving and Programming.")
    print("Note: This software is strictly for educational purposes.")

    while True:
        try:
            display_menu()
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                handle_new_blood_test(session_records, sample_counter)
                sample_counter += 1
            elif choice == '2':
                view_all_records(session_records)
            elif choice == '3':
                search_records_interactive(session_records)
            elif choice == '4':
                display_reference_ranges()
            elif choice == '5':
                display_about()
            elif choice == '6':
                print("\nThank you for using Blood Cell Count Analyzer.")
                print("Exiting application. Have a great day!\n")
                break
            else:
                print("\n>> Error: Invalid selection. Please enter a number between 1 and 6.")
                
        except KeyboardInterrupt:
            print("\n\nOperation interrupted by user. Exiting application gracefully...")
            break
        except Exception as e:
            print(f"\n>> An unexpected error occurred: {e}")
            print(">> Returning safely to the main menu.\n")

if __name__ == "__main__":
    main()
