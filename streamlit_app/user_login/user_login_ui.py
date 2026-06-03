import streamlit as st
from user_login.user_login import  login_user

def login_page():

    st.subheader("Login Page")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        success, message = login_user(
            email,
            password
        )

        if success:
            st.success(message)
            st.session_state.page = "report"
            st.rerun()
        else:
            st.error(message)
            return None
    