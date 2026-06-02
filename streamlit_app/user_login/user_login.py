import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from snowflake_connection.snowflake_con import get_connection

def login_user(email, password):

    conn = get_connection()
    cur = conn.cursor()

    try:

        cur.execute(
            """
            SELECT FIRST_NAME,
                   LAST_NAME
            FROM STM.ADM.USERS 
            WHERE EMAIL = %s
            AND PASS = %s
            """,
            (email, password)
        )

        user = cur.fetchone()

        if user:
            return True, f"Welcome {user[0]} {user[1]}"

        return False, "Invalid Credentials"

    except Exception as e:
        return False, str(e)

    finally:
        cur.close()
        conn.close()