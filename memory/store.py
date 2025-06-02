import sqlite3
import os

def save_to_memory(prompt: str, model_path: str):
    os.makedirs("memory", exist_ok=True)
    conn = sqlite3.connect("memory/memory.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt TEXT,
            model_path TEXT
        )
    ''')
    c.execute("INSERT INTO memory (prompt, model_path) VALUES (?, ?)", (prompt, model_path))
    conn.commit()
    conn.close()
