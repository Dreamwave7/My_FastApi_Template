from sqlalchemy import insert, delete, select, update, func, and_
from sqlalchemy.ext.asyncio import AsyncSession
from models import UserModel
from users.schemas import UserRegister


class BaseActions:
    @staticmethod
    async def find_user_or_none(session: AsyncSession, user_email:str):
        query = select(UserModel).filter(UserModel.email == user_email)
        result = await session.execute(query)
        return result.one_or_none()
    
    @staticmethod
    async def add(session:AsyncSession, user:UserRegister):
        query = insert(UserModel).values(**user.model_dump()).returning(UserModel.email)
        result = await session.execute(query)
        return result.mappings().first()
    


