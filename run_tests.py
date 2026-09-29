# run_tests.py
# Automated verification test script for Blood Cell Count Analyzer
# Course: CSE1021 - Introduction to Problem Solving and Programming
# Author: Isha Singh Rajput

"""
Runs automated test cases to check value classifications, boundary cutoffs,
summary counters, and linear search without having to re-type in the terminal.
"""

from analyzer import analyze_blood_values, classify_value
from records import search_by_name, search_by_sample_id

def run_all_tests():
    print("=" * 65)
    print("      RUNNING AUTOMATED TEST SUITE FOR BLOOD CELL COUNT ANALYZER")
    print("=" * 65)
    
    passed_tests = 0
    total_tests = 5

    # -------------------------------------------------------------
    # TEST CASE 1: All values within range
    # -------------------------------------------------------------
    print("\n[TEST CASE 1] All values within range")
    tc1_data = {"RBC": 5.0, "WBC": 7000.0, "Platelets": 250000.0}
    tc1_res = analyze_blood_values(tc1_data, "Male")
    tc1_summary = tc1_res["summary"]
    
    rbc_stat = tc1_res["parameters"][0]["status"]
    wbc_stat = tc1_res["parameters"][1]["status"]
    plt_stat = tc1_res["parameters"][2]["status"]
    
    assert rbc_stat == "WITHIN RANGE", f"Expected WITHIN RANGE, got {rbc_stat}"
    assert wbc_stat == "WITHIN RANGE", f"Expected WITHIN RANGE, got {wbc_stat}"
    assert plt_stat == "WITHIN RANGE", f"Expected WITHIN RANGE, got {plt_stat}"
    assert tc1_summary["within_range"] == 3
    assert tc1_summary["low"] == 0
    assert tc1_summary["high"] == 0
    print("  -> RBC: 5.0 (WITHIN RANGE), WBC: 7000 (WITHIN RANGE), Platelets: 250000 (WITHIN RANGE)")
    print("  -> Summary: Within=3, Low=0, High=0")
    print("  [PASSED] Test Case 1 Successful.")
    passed_tests += 1

    # -------------------------------------------------------------
    # TEST CASE 2: One value below range (e.g., RBC below range)
    # -------------------------------------------------------------
    print("\n[TEST CASE 2] One value below range (RBC Low)")
    tc2_data = {"RBC": 3.5, "WBC": 6500.0, "Platelets": 220000.0}
    tc2_res = analyze_blood_values(tc2_data, "Male") # Male min is 4.5
    tc2_summary = tc2_res["summary"]
    
    assert tc2_res["parameters"][0]["status"] == "LOW", "RBC should be LOW"
    assert tc2_res["parameters"][1]["status"] == "WITHIN RANGE", "WBC should be WITHIN RANGE"
    assert tc2_res["parameters"][2]["status"] == "WITHIN RANGE", "Platelets should be WITHIN RANGE"
    assert tc2_summary["within_range"] == 2
    assert tc2_summary["low"] == 1
    assert tc2_summary["high"] == 0
    print("  -> RBC: 3.5 (LOW), WBC: 6500 (WITHIN RANGE), Platelets: 220000 (WITHIN RANGE)")
    print("  -> Summary: Within=2, Low=1, High=0")
    print("  [PASSED] Test Case 2 Successful.")
    passed_tests += 1

    # -------------------------------------------------------------
    # TEST CASE 3: One value above range (e.g., WBC High)
    # -------------------------------------------------------------
    print("\n[TEST CASE 3] One value above range (WBC High)")
    tc3_data = {"RBC": 4.8, "WBC": 13500.0, "Platelets": 300000.0}
    tc3_res = analyze_blood_values(tc3_data, "Female")
    tc3_summary = tc3_res["summary"]
    
    assert tc3_res["parameters"][0]["status"] == "WITHIN RANGE", "RBC should be WITHIN RANGE"
    assert tc3_res["parameters"][1]["status"] == "HIGH", "WBC should be HIGH"
    assert tc3_res["parameters"][2]["status"] == "WITHIN RANGE", "Platelets should be WITHIN RANGE"
    assert tc3_summary["within_range"] == 2
    assert tc3_summary["low"] == 0
    assert tc3_summary["high"] == 1
    print("  -> RBC: 4.8 (WITHIN RANGE), WBC: 13500 (HIGH), Platelets: 300000 (WITHIN RANGE)")
    print("  -> Summary: Within=2, Low=0, High=1")
    print("  [PASSED] Test Case 3 Successful.")
    passed_tests += 1

    # -------------------------------------------------------------
    # TEST CASE 4: Multiple abnormal values (RBC low, WBC high, Platelets low)
    # -------------------------------------------------------------
    print("\n[TEST CASE 4] Multiple abnormal values (RBC Low, WBC High, Platelets Low)")
    tc4_data = {"RBC": 3.8, "WBC": 14200.0, "Platelets": 110000.0}
    tc4_res = analyze_blood_values(tc4_data, "Male")
    tc4_summary = tc4_res["summary"]
    
    assert tc4_res["parameters"][0]["status"] == "LOW", "RBC should be LOW"
    assert tc4_res["parameters"][1]["status"] == "HIGH", "WBC should be HIGH"
    assert tc4_res["parameters"][2]["status"] == "LOW", "Platelets should be LOW"
    assert tc4_summary["within_range"] == 0
    assert tc4_summary["low"] == 2
    assert tc4_summary["high"] == 1
    print("  -> RBC: 3.8 (LOW), WBC: 14200 (HIGH), Platelets: 110000 (LOW)")
    print("  -> Summary: Within=0, Low=2, High=1")
    print("  [PASSED] Test Case 4 Successful.")
    passed_tests += 1

    # -------------------------------------------------------------
    # TEST CASE 5: Validation logic verification (negative, zero, classification)
    # -------------------------------------------------------------
    print("\n[TEST CASE 5] Boundary condition and classification logic")
    # Exact boundary checks
    assert classify_value(4.5, 4.5, 5.9) == "WITHIN RANGE", "Boundary min should be WITHIN RANGE"
    assert classify_value(5.9, 4.5, 5.9) == "WITHIN RANGE", "Boundary max should be WITHIN RANGE"
    assert classify_value(4.49, 4.5, 5.9) == "LOW", "Below min should be LOW"
    assert classify_value(5.91, 4.5, 5.9) == "HIGH", "Above max should be HIGH"
    
    # Linear search verification
    dummy_records = [
        {"patient_info": {"sample_id": "SMP-1001", "name": "Rahul Sharma", "age": 19, "gender": "Male"}},
        {"patient_info": {"sample_id": "SMP-1002", "name": "Priya Patel", "age": 20, "gender": "Female"}}
    ]
    search_res = search_by_name(dummy_records, "Rahul")
    assert len(search_res) == 1 and search_res[0]["patient_info"]["name"] == "Rahul Sharma"
    
    id_res = search_by_sample_id(dummy_records, "SMP-1002")
    assert len(id_res) == 1 and id_res[0]["patient_info"]["name"] == "Priya Patel"
    
    non_existent = search_by_name(dummy_records, "Vikram")
    assert len(non_existent) == 0

    print("  -> Verified min boundary (4.5 -> WITHIN RANGE)")
    print("  -> Verified max boundary (5.9 -> WITHIN RANGE)")
    print("  -> Verified below boundary (4.49 -> LOW)")
    print("  -> Verified above boundary (5.91 -> HIGH)")
    print("  -> Verified linear search by name and sample ID")
    print("  [PASSED] Test Case 5 Successful.")
    passed_tests += 1

    print("\n" + "=" * 65)
    print(f"TEST RESULTS: {passed_tests}/{total_tests} TEST CASES PASSED SUCCESSFULLY (100%)")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    run_all_tests()
