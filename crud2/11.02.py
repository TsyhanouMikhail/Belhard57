import sqlite3
# что то пошло не так
class CRUDCategory:

    @staticmethod
    def create_session(func):
        def wrapper(**kwargs):
            conn = sqlite3.connect("../db.db")
            cur = conn.cursor()
            return  func(**kwargs, cur=cur, conn=conn)
        return wrapper

    @staticmethod
    @create_session
    def add(name: str, cur=None, conn=None) -> tuple:
        cur.execute("""
            INSERT INTO categories(name)
            VALUES(?);
        """, (name, ))
        conn.commit()


CRUDCategory.add(name="авто-детали")

#



