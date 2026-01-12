"""
save_test_case_spec.py
----------------------
Lưu test case spec vào thư mục resource/test_case_spec/<req_id>.
"""

import json
import os
import uuid

def run(req_id: str, testcase: dict):
    base = f"./resources/test_case_spec/{req_id}"
    os.makedirs(base, exist_ok=True)
    print("Saving test case with ID:", testcase)
    tc_id = testcase['id'] or str(uuid.uuid4())
    
    # testcase['id']
    path = os.path.join(base, f"{tc_id}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(testcase, f, indent=4)

    return {"status": "saved", "location": path}

# import json
# import os

# def run(req_id: str, testcase: dict):
#     base = f"./resources/test_case_spec/{req_id}"
#     os.makedirs(base, exist_ok=True)

#     # Validate dictionary
#     if not isinstance(testcase, dict):
#         return {
#             "status": "error",
#             "reason": "testcase is not a valid dict",
#             "raw": str(testcase)
#         }

#     # Determine test case identifier
#     tc_id = None

#     if "tc_id" in testcase and isinstance(testcase["tc_id"], str) and testcase["tc_id"].strip():
#         tc_id = testcase["tc_id"].strip()

#     elif "id" in testcase and isinstance(testcase["id"], str) and testcase["id"].strip():
#         tc_id = testcase["id"].strip()

#     else:
#         # Nếu cả hai không có → báo lỗi rõ ràng
#         return {
#             "status": "error",
#             "reason": "Missing both tc_id and id in testcase",
#             "raw": testcase
#         }

#     # Save JSON
#     path = os.path.join(base, f"{tc_id}.json")

#     try:
#         with open(path, "w", encoding="utf-8") as f:
#             json.dump(testcase, f, indent=4)

#         return {"status": "saved", "tc_id": tc_id, "location": path}

#     except Exception as e:
#         return {
#             "status": "error",
#             "reason": f"Failed to write file: {str(e)}",
#             "raw": testcase
#         }
