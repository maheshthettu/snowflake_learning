import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from snowflake_connection.snowflake_con import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT CURRENT_USER(), CURRENT_ROLE(), CURRENT_DATABASE()")
print(cur.fetchone())

cur.close()
conn.close()