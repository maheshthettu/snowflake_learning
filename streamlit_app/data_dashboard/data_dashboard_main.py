import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
def dashboard_page(): 
    st.markdown(
    """
    <h3>Dash Board Page</h3>
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

    dash_page = st.sidebar.selectbox(
        "Event",
        ["Student", "Cars"]
    )

    # if dash_page == "Student":
    #     login_page()

    # elif dash_page == "Cars":
    #     register_page()