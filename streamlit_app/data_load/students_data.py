import streamlit as st
import tempfile
import os
import pandas as pd
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))
from snowflake_connection.snowflake_con import get_connection


def upload_csv_to_snowflake_stage():

    st.subheader("📚 Students Data Upload")

    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        type=["csv"]
    )

    if uploaded_file:

        st.success(f"Selected file: {uploaded_file.name}")

        # Preview file
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

        if st.button("Upload to Snowflake Stage"):

            temp_file_path = None
            conn = None

            try:
                # Save file temporarily
                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".csv"
                ) as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    temp_file_path = tmp_file.name

                temp_file_path = temp_file_path.replace("\\", "/")

                conn = get_connection()
                stage_name = "STM.ADM.STUDENT_DATA_STAGE"

                with conn.cursor() as cursor:

                    put_sql = f"""
                    PUT 'file:///{temp_file_path}'
                    @{stage_name}
                    AUTO_COMPRESS=TRUE
                    OVERWRITE=TRUE
                    """

                    cursor.execute(put_sql)
                    cursor.execute("ALTER PIPE STM.ADM.STUDENTS_PIPE REFRESH")
                    # Show files in stage
                    st.success(
                        f"{uploaded_file.name} data is loaded successfully to snowflake"
                    )



            except Exception as e:
                st.error(f"Upload failed: {str(e)}")

            finally:
                # cleanup temp file
                if temp_file_path and os.path.exists(temp_file_path):
                    os.remove(temp_file_path)

                # close connection safely
                if conn:
                    try:
                        conn.close()
                    except:
                        pass