import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from  data_load.students_data import upload_csv_to_snowflake_stage
def data_load(): 
    st.markdown(
    """
    <h3>Data Loading Page</h3>
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

    load_page = st.sidebar.selectbox(
        "Event",
        ["Student", "Cars"]
    )

    if load_page == "Student":
        upload_csv_to_snowflake_stage()

    # elif load_page == "Cars":
    #     register_page()