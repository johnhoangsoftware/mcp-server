"""
load_requirement.py
-------------------
Parse requirement từ Excel → normalize theo requirement.schema.json.
Không xử lý logic chia nhỏ — chỉ load raw + normalize.
"""

from parsers.excel_parser import parse_excel_requirement

def run(req_id: str):
    path = f"./resources/requirements/{req_id}.xlsx"
    requirement = parse_excel_requirement(path)

    return {
        "id": req_id,
        "title": requirement["title"],
        "description": requirement["description"],
        "acceptance_criteria": requirement["acceptance_criteria"]
    }
