from sqlalchemy import insert, delete, select, update, func
from sqlalchemy.ext.asyncio import AsyncSession
from models import UserModel


class BaseActions:
    @classmethod
    async def find_user_or_none(session: AsyncSession, *filter):
        query = select(UserModel).filter(*filter)
        result = await session.execute(query)
        return result.scalars().one_or_none()
    