from typing import Optional, List, Tuple
from sqlalchemy import select, update, delete
# from sqlalchemy.orm import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import create_async_session, Category, Article

from schemas import CategorySchema, CategoryInDBSchema


class CRUDCategory:

    @staticmethod
    @create_async_session
    async def add(category: CategorySchema, session: AsyncSession = None) -> Optional[CategoryInDBSchema]:
        # name: str, parent_id: int, session: AsyncSession = None) -> Optional[Category]:
        category = Category(**category.dict())
        # category = Category(name=name, parent_id=parent_id)
        session.add(category)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(category)
            return CategoryInDBSchema(**category.__dict__)
            # return category

    @staticmethod
    @create_async_session
    async def get(category_id: int, session: AsyncSession = None) -> Optional[CategoryInDBSchema]:
        category = await session.execute(
            select(Category)
            .where(Category.id == category_id)
        )
        category = category.first()
        if category:
            return CategoryInDBSchema(**category[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(parent_id: int = None, session: AsyncSession = None) -> List[CategoryInDBSchema]:
        if parent_id:
            categories = await session.execute(
                select(Category)
                .where(Category.parent_id == parent_id)
                .order_by(Category.id)
            )
        else:

            categories = session.execute(
                select(Category)
                .order_by(Category.id)
            )
        return [CategoryInDBSchema(**category[0].__dict__) for category in categories]

    @staticmethod
    @create_async_session
    async def delete(category_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Category)
            .where(Category.id == category_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(
            category: CategoryInDBSchema,
            # category_id: int,
            # name: str = None,
            # parent_id: int = None,
            session: AsyncSession = None

    ) -> bool:
        await session.execute(
            update(Category)
            .where(Category.id == category.id)
            # .where(Category.id == category_id)
            .values(**category.dict()
                    # name=name if name else Category.name,
                    # parent_id=parent_id if parent_id else Category.parent_id
                    )
        )
        try:
            await session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_async_session
    async def get_articles(category_id: int, session: AsyncSession = None) -> List[Tuple[Category, Article]]:
        response = await session.execute(
            select(Category, Article)
            .join(Article, Category.id == Article.category_id)
            .where(Category.id == category_id)
        )
        return response.all()

    #

# User, Category, Article, ArticleComment,
