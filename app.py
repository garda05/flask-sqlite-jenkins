from flask import Flask, jsonify
import os
import sqlite3

app = Flask(__name__)
DB_PATH = os.getenv("DB_PATH", "/data/app.db")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS visits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL
            )
        """)
        count = conn.execute("SELECT COUNT(*) FROM visits").fetchone()[0]
        if count == 0:
            conn.execute("INSERT INTO visits (message) VALUES (?)",
                         ("Database SQLite berhasil terhubung",))

@app.route("/")
def home():
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute("SELECT id, message FROM visits").fetchall()
    return jsonify({
        "application": "Modul 2 Komputasi Awan",
        "message": "Halo dari Flask + Docker + Jenkins!",
        "database": "SQLite",
        "records": [{"id": row[0], "message": row[1]} for row in rows]
    })

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
