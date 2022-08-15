from crud import CRUDCategory
import asyncio

import threading
from time import sleep

from crud import  CRUDCategory

async def main():
    res = await CRUDCategory.get_all()
    print(res)



# category = CRUDCategory.get(category_id=1)
# print(category)
# category.name = "Еда"
# CRUDCategory.update(category=category)
# print(CRUDCategory.get(category_id=1))


#
#
# def main():
#     for i in range(1, 101):
#         print(i)
#         sleep(1)
#
# if __name__ == '__main__':
#     threads = []
#     for _ in range(10):
#         threads.append((threading.Thread(target=mail)))
#     for thread in threads:
#         thread.start()



# category.parent_id = None


# CRUDCategory.add(name="Стеки", parent_id=1)
# CRUDCategory.add(name="Ролы", parent_id=2)
# for category in CRUDCategory.get_all():
#     print(category.name)
#     print(category.__dict__)