import sys
import os

# `app`ディレクトリをモジュール検索パスに追加
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from database import get_db_connection

# DDLディレクトリ
DDL_DIR = "./ddl"

def execute_ddl_scripts():
    conn = get_db_connection()
    cur = conn.cursor()

    # DDLスクリプトを順次実行
    scripts = sorted([f for f in os.listdir(DDL_DIR) if f.endswith('.sql')])
    for script in scripts:
        script_path = os.path.join(DDL_DIR, script)
        with open(script_path, 'r') as file:
            sql = file.read()
            cur.execute(sql)
            conn.commit()
            print(f'Executed {script}')

    cur.close()
    conn.close()
    print("All DDL scripts executed successfully.")

def run_application():
    from main import fetch_users
    fetch_users()

if __name__ == "__main__":
    execute_ddl_scripts()
    run_application()
