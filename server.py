"""
server.py
---------
Entry point của MCP server.
- Load tools
- Expose tool definitions
- Bind JSON-RPC server
"""
# from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP
from tools import (
    list_requirements,
    load_requirement,
    extract_testable_units,
    generate_test_case_spec,
    save_test_case_spec,
)

app = FastMCP("mcp-demo")


@app.tool()
def list_requirements_tool():
    return list_requirements.run()


@app.tool()
def load_requirement_tool(id: str):
    return load_requirement.run(id)


@app.tool()
def extract_testable_units_tool(requirement: dict):
    return extract_testable_units.run(requirement)


@app.tool()
def generate_test_case_spec_tool(testable_unit: dict):
    return generate_test_case_spec.run(testable_unit)


@app.tool()
def save_test_case_spec_tool(test_case_spec: dict):
    return save_test_case_spec.run(test_case_spec)


if __name__ == "__main__":
    app.run()
