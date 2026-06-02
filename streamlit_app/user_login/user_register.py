import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from snowflake_connection.snowflake_con import get_connection

def user_register(
    first_name,
    last_name,
    email,
    phone_number,
    password
):
    conn = get_connection()
    cur = conn.cursor()

    try:

        cur.execute(
            """
            SELECT EMAIL
            FROM STM.ADM.USERS
            WHERE EMAIL = %s
            """,
            (email,)
        )

        if cur.fetchone():
            return False, "Email already exists"

        cur.execute(
            """
            INSERT INTO STM.ADM.USERS
            (
                FIRST_NAME,
                LAST_NAME,
                EMAIL,
                PHONE_NUMBER,
                PASS
            )
            VALUES
            (%s,%s,%s,%s,%s)
            """,
            (
                first_name,
                last_name,
                email,
                phone_number,
                password
            )
        )

        conn.commit()

        return True, "Registration Successful"

    except Exception as e:
        return False, str(e)

    finally:
        cur.close()
        conn.close()