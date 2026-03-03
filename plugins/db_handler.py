cat <<EOF > ~/Hhdo/db_handler.py
import sqlite3

db = sqlite3.connect("crystal.db", check_same_thread=False)
cr = db.cursor()

def start_db():
    # جدول المستخدمين والرسائل
    cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, msgs INTEGER DEFAULT 0)")
    # جدول المطورين (سودو)
    cr.execute("CREATE TABLE IF NOT EXISTS sudos (user_id INTEGER PRIMARY KEY)")
    db.commit()

start_db()

def is_sudo(user_id):
    cr.execute("SELECT user_id FROM sudos WHERE user_id = ?", (user_id,))
    return cr.fetchone() is not None
EOF
