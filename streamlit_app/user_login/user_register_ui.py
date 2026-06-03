
import sys
from pathlib import Path
import streamlit as st
sys.path.append(str(Path(__file__).resolve().parents[1]))
from snowflake_connection.snowflake_con import get_connection
from user_login.user_register import user_register
from streamlit_app.user_login.user_validaters import validate_user

def register_page():

    st.subheader("Register")

    col1, col2 = st.columns(2)

    with col1:
        first_name = st.text_input("First Name")
        email = st.text_input("Email")
        password = st.text_input(
            "Password",
            type="password"
        )

    with col2:
        last_name = st.text_input("Last Name")
        phone_number = st.text_input("Phone Number")
        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

    if st.button("Register"):

        if password != confirm_password:
            st.error("Passwords do not match")
            return

        conn = get_connection()

        validation_error = validate_user(
            conn,
            email,
            phone_number
        )

        if validation_error:
            st.error(validation_error)
            return

        success, message = user_register(
            first_name,
            last_name,
            email,
            phone_number,
            password
        )

        if success:
            st.success(message)
            st.session_state.page = "login"
            st.rerun()
        else:
            st.error(message)