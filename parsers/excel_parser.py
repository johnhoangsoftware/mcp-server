"""
excel_parser.py
----------------
Parser mẫu — lấy title, description, acceptance criteria.
"""

import openpyxl

def parse_excel_requirement(path: str):
    wb = openpyxl.load_workbook(path)
    sheet = wb.active

    return {
        "title": sheet["A2"].value,
        "description": sheet["B2"].value,
        "acceptance_criteria": [
            sheet["C2"].value,
            sheet["C3"].value
        ]
    }
