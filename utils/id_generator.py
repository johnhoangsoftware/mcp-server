"""
id_generator.py
----------------
Sinh ID dạng TU_R1_01, TC_R1_01
"""

counter_tu = {}
counter_tc = {}

def generate_tu_id(req_id):
    counter_tu.setdefault(req_id, 0)
    counter_tu[req_id] += 1
    return f"TU_{req_id}_{counter_tu[req_id]:02d}"

def generate_tc_id(req_id):
    counter_tc.setdefault(req_id, 0)
    counter_tc[req_id] += 1
    return f"TC_{req_id}_{counter_tc[req_id]:02d}"
