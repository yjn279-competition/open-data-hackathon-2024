from database import get_db_connection

def fetch_users():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, username, created_at FROM users")
    rows = cur.fetchall()

    for row in rows:
        print(f"ID: {row[0]}, Username: {row[1]}, Created At: {row[2]}")

    cur.close()
    conn.close()

if __name__ == "__main__":
    print("Fetching users from the database...")
    fetch_users()
