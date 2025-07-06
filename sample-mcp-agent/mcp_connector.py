import json

def load_mcp_data(filepath="test_data/sample_mcp.json"):
    """
    Loads MCP user financial data from a JSON file.
    """
    try:
        with open(filepath, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("❌ MCP data file not found.")
        return {}