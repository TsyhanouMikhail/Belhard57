import sqlite3

conn = sqlite3.connect("../db.db")
cur = conn.cursor()
cur.execute("""
    ALTER TABLE users
    DROP age;
""")


conn.commit()


# cur.execute("""
#     SELECT articles.title, articles.body, categories.name
#     FROM articles
#     JOIN categories
#     ON articles.category_id = categories.id;
#
# """)
#
# print(cur.fetchall())
# # conn.commit()
