cat <<EOF > ~/Hhdo/db_handler.py
import sqlite3

db = sqlite3.connect("crystal.db", check_same_thread=False)
cr = db.cursor()

def start_db():
    cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, msgs INTEGER DEFAULT 0, rank TEXT DEFAULT 'member')")
    cr.execute("CREATE TABLE IF NOT EXISTS groups (chat_id INTEGER PRIMARY KEY, status TEXT DEFAULT 'on')")
    db.commit()

start_db()
EOF
