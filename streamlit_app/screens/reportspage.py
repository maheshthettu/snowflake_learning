import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from data_dashboard.data_dashboard_main import dashboard_page
from data_load.data_load_main import data_load
def report_page(): 
    st.markdown(
    """
    <h1>Report Page</h1>
    """,
    unsafe_allow_html=True
)

    st.markdown("""
    <style>
    /* Login Menu label */
    .stSelectbox label {
        font-size: 10px !important;
        font-weight: bold !important;
    }

    /* Selected value inside dropdown */
    .stSelectbox div[data-baseweb="select"] > div {
        font-size: 15px !important;
    }

    /* Dropdown options */
    div[role="listbox"] div {
        font-size: 22px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    report_page = st.sidebar.selectbox(
        "Report Menu",
        ["Dash Board", "Data Loading"]
    )

    if report_page == "Dash Board":
        dashboard_page()

    elif report_page == "Data Loading":
        data_load()