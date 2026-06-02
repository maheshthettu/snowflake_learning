import streamlit as st
from screens.landingpage import landing_page
from screens.reportspage import report_page
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from streamlit_app.user_login_ui.user_login_ui import login_page


if "page" not in st.session_state:
    st.session_state.page = "landingpage"

if st.session_state.page == "landingpage":
    landing_page()
elif st.session_state.page == "login":
    login_page()
elif st.session_state.page == "report":
    report_page()







