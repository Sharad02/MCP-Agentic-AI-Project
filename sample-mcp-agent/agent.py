import json

def get_net_worth(mcp_data):
    total_assets = sum(mcp_data["assets"].values())
    total_liabilities = sum(mcp_data["liabilities"].values())
    return total_assets - total_liabilities

if __name__ == "__main__":
    with open("test_data/sample_mcp.json") as f:
        data = json.load(f)
    net_worth = get_net_worth(data)
    print(f"Your net worth is ₹{net_worth}")
