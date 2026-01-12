"""
extract_testable_units.py
-------------------------
Tool phân tích requirement (đã chuẩn hóa) để sinh Testable Units (TU).
- TU = "minimum verifiable behavior"
- Dùng LLM để phân tích logic, điều kiện, rẽ nhánh
"""

from llm_client import call_llm

schema = {
    "input": {"requirement_text": "string"},
    "output": {"testable_units": "list"}
}

def run(requirement_text: str):
    prompt = f"""
You are a senior QA system.
Analyze the following requirement and break it down into Testable Units.
A Testable Unit is the smallest behavior that can be independently verified.

Requirement:
{requirement_text}

Return JSON:
[
  {{
    "id": "TU1",
    "title": "...",
    "description": "...",
    "preconditions": [...],
    "postconditions": [...],
    "risks": [...]
  }},
  ...
]
"""
    result = call_llm(prompt)
    return {"testable_units": result}
