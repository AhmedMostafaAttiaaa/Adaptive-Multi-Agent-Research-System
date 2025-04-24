import sqlite3

# Initialize the database and create required tables
def init_db():
    conn = sqlite3.connect("ai_project.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        input TEXT,
        output TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')

    conn.commit()
    conn.close()

# Log each user interaction with the AI system
def log_interaction(user_id, user_input, result):
    conn = sqlite3.connect("ai_project.db")
    c = conn.cursor()
    c.execute("INSERT INTO logs (user_id, input, output) VALUES (?, ?, ?)", (user_id, user_input, result))
    conn.commit()
    conn.close()

# Verify user credentials for login
def verify_user(username, password):
    conn = sqlite3.connect("ai_project.db")
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE username=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    return user[0] if user else None
