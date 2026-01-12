"""
generate_test_case_spec.py
--------------------------
Tool dùng LLM để tạo Test Case Specification từ Testable Units.
- LLM phải reasoning sâu
- Tách rõ từng step
- Bao gồm data set, negative cases, boundary, exception
"""

from unittest import result
from llm_client import call_llm

schema = {
    "input": {"testable_units": "list"},
    "output": {"test_cases": "list"}
}

# def run(testable_units: list):
#     prompt = f"""
# You are a world-class test architect.
# Generate complete Test Case Specifications for the following Testable Units:

# {testable_units}

# Rules:
# 1. Each Testable Unit must produce 1..N test cases.
# 2. Each test case must contain:
#    - id
#    - objective
#    - preconditions
#    - steps
#    - expected_result
#    - data_matrix (MUST)
#    - negative cases (MUST)
#    - boundary conditions (MUST)

# Return JSON ONLY.
# """
#     result = call_llm(prompt)
#     return {"test_cases": result}

import json

def run(testable_units: list):
    prompt = f"""
You are a world-class test architect.

Generate Test Cases for the following Testable Units:
{testable_units}

STRICT OUTPUT RULES (MANDATORY):
- Return ONLY valid JSON
- Do NOT use markdown
- Do NOT include explanations or comments
- Do NOT include ``` or ```json
- All string values MUST be single-line
- All arrays MUST be present even if empty
- JSON must be directly parseable by json.loads()

EACH TEST CASE MUST FOLLOW THIS SCHEMA EXACTLY:
{{
  "tc_id": "string",
  "objective": "string",
  "precondition": "string",
  "dataset": ["string"],
  "steps": ["string"],
  "expected": ["string"],
  "trace": "string",
  "type": "string"
}}

ADDITIONAL RULES:
1. Output MUST be a JSON array of test cases
2. Each Testable Unit MUST generate at least one test case
3. "type" MUST be one of: "functional", "negative", "boundary", "security", "usability"
4. "trace" MUST reference the Testable Unit identifier
5. "dataset", "steps", and "expected" MUST contain at least one item
6. Do NOT invent fields outside the schema
7. Do NOT omit any field

Return JSON ONLY.
"""

    result = call_llm(prompt)

    # Hard safety check (recommended)
    #return json.loads(result)
    return {"test_cases": result}
