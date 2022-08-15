import sqlite3

conn = sqlite3.connect("../db.db")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(24) UNIQUE NOT NULL,
        parent_id INTEGER,
        FOREIGN KEY (parent_id) REFERENCES categories(id)

    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS roles(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
        
    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login VARCHAR(45) UNIQUE NOT NULL,
        password VARCHAR(50) NOT NULL,
        email VARCHAR(45) UNIQUE NOT NULL,
        role_id INTEGER NOT NULL,
        FOREIGN KEY (role_id) REFERENCES roles(id)

    );
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS articles(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(24) NOT NULL,
        body VARCHAR(140) NOT NULL,
        category_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (category_id) REFERENCES categories(id),
        FOREIGN KEY (user_id) REFERENCES users(id)

    );
""")
conn.commit()
