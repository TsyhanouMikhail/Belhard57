from engine import create_session

class CRUDCategory:

    @staticmethod
    @create_session
    def add(name: str, cur=None, conn=None) -> tuple:
        cur.execute("""
            INSERT INTO categories(name)
            VALUES(?);
        """, (name, ))
        conn.commit()

    @staticmethod
    @create_session
    def get(category_id: int, cur=None, conn=None) -> tuple:
        cur.execute("""
            SELECT * FROM categories
            WHERE id = ?;
        """, (category_id, ))
        return cur.fetchone()



print(CRUDCategory.get(category_id=3))
# CRUDCategory.add(name="авто-детали")