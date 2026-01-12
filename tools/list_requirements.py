"""
list_requirements.py
--------------------
Trả danh sách file requirement có trong thư mục resources/requirements.
LLM sẽ gọi tool này đầu tiên để biết có những req nào.
"""

import os

def run():
    base = "./resources/requirements"
    files = os.listdir(base)
    return [{"id": f.replace(".xlsx", ""), "filename": f} for f in files]
