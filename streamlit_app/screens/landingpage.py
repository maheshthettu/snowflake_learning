import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from streamlit_app.user_login_ui.user_login_ui import login_page
from streamlit_app.user_login_ui.user_register_ui import register_page

def landing_page(): 
    
    st.markdown(
    """
    <h2>Snowflake Data Engineering Project</h2>
    """,
    unsafe_allow_html=True
)
    
    st.markdown("""
    <style>
    /* Login Menu label */
    .stSelectbox label {
        font-size: 1px !important;
        font-weight: bold !important;
    }

    /* Selected value inside dropdown */
    .stSelectbox div[data-baseweb="select"] > div {
        font-size: 22px !important;
    }

    /* Dropdown options */
    div[role="listbox"] div {
        font-size: 22px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    option = st.sidebar.selectbox(
        "Login Menu",
        ["Login", "Register"]
    )


    if option == "Login":
        login_page()

    elif option == "Register":
        register_page()
    
