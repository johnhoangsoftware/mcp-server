"""
run_demo.py
------------
Demo end-to-end MCP pipeline (Requirement → TU → Test Case Spec)
Chạy trực tiếp mà không cần MCP SDK
"""

from tools import (
    list_requirements,
    load_requirement,
    extract_testable_units,
    generate_test_case_spec,
    save_test_case_spec
)

def main():
    # 1️⃣ Liệt kê requirement
    reqs = list_requirements.run()
    print("Available requirements:", reqs)

    # Chọn requirement đầu tiên
    req_id = reqs[0]["id"]
    print("Processing requirement:", req_id)

    # 2️⃣ Load requirement
    requirement = load_requirement.run(req_id)
    print("Requirement loaded:", requirement)

    # 3️⃣ Extract Testable Units (LLM reasoning)
    TU_list = extract_testable_units.run(requirement["description"])
    print("Testable Units generated:", TU_list)

    # 4️⃣ Generate Test Case Spec (LLM reasoning)
    test_cases = generate_test_case_spec.run(TU_list)
    print("Test Case Specs generated:", test_cases)

    # 5️⃣ Save test case spec
    for tc in test_cases["test_cases"]:
        save_result = save_test_case_spec.run(req_id, tc)
        print("Saved:", save_result)

if __name__ == "__main__":
    main()