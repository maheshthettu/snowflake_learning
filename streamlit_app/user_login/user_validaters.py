import re


def is_valid_email(email: str) -> bool:
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return bool(re.match(pattern, email))


def is_valid_phone(phone: str) -> bool:
    return phone.isdigit() and len(phone) == 10


def validate_user(conn, email: str, phone: str):

    # Email format validation
    if not is_valid_email(email):
        return "Invalid email format"

    # Phone validation
    if not is_valid_phone(phone):
        return "Phone number must contain exactly 10 digits"

    cur = conn.cursor()

    try:

        # Email exists
        cur.execute(
            """
            SELECT 1
            FROM STM.ADM.USERS
            WHERE EMAIL = %s
            """,
            (email,)
        )

        if cur.fetchone():
            return "Email already exists"

        # Phone exists
        cur.execute(
            """
            SELECT 1
            FROM STM.ADM.USERS
            WHERE PHONE_NUMBER = %s
            """,
            (phone,)
        )

        if cur.fetchone():
            return "Phone number already exists"

        return None

    finally:
        cur.close()