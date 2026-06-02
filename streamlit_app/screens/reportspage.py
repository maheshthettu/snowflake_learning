import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
def report_page(): 
    st.markdown(
    """
    <h1>Snowflake Data Engineering Project</h1>
    """,
    unsafe_allow_html=True
)
    st.markdown(
    """
    <h3>Report Page</h3>
    """,
    unsafe_allow_html=True
)
