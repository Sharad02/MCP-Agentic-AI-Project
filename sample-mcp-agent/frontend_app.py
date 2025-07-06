import streamlit as st
from mcp_connector import load_mcp_data
from agent import get_net_worth

st.set_page_config(page_title="MCP Agentic AI", layout="centered")

st.title("🧠 MCP Agentic AI Demo")
st.markdown("Ask financial questions based on your structured data (MCP)")

data = load_mcp_data()

if not data:
    st.error("Could not load MCP data.")
else:
    st.success("✅ MCP data loaded!")

    if st.button("What is my net worth?"):
        result = get_net_worth(data)
        st.markdown(f"**Your net worth is:** ₹{result:,}")

    # Add more queries here later
