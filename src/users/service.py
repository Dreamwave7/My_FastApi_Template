from sqlalchemy import insert, values, delete
from passlib.context import CryptContext
from users.schemas import UserRegister
from database import Session
from models import UserModel
from objects import BaseActions
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from config import settings

import jwt
context = CryptContext(schemes=["bcrypt"])

class AuthService:
    @staticmethod
    def get_password_hash(password:str):
        return context.hash(password)
    
    @staticmethod
    def verify_password(ordinary_password:str, hashed_password:str):
        return context.verify(ordinary_password, hashed_password)
    
    @staticmethod
    async def create_token(user_id:int):
        pass

    @staticmethod
    async def create_access_token(user_email:str):
        to_encode = {
            "sub": str(user_email),
            "exp": datetime.utcnow() + timedelta(days=4)}
        encoded_token = jwt.encode(to_encode,settings.SECRET_KEY,algorithm=settings.ALGORITHM)
        return encoded_token

    @staticmethod
    async def check_user(email:str, password:str):
        async with Session() as connect:
            user_exist = await BaseActions.find_user_or_none(connect, email)

            if user_exist:
                user_hashed_password = user_exist[0].password
                verifying_password = AuthService.verify_password(password,user_hashed_password)
                if verifying_password:
                    return True
                else:
                    return None
                


 
        


class UserService:
    @staticmethod
    async def register_new_user(user: UserRegister):
        async with Session() as connect:
            user_exist = await BaseActions.find_user_or_none(connect, user.email)
            if user_exist:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exist")
            
            user.password = AuthService.get_password_hash(user.password)
            reg_user = await BaseActions.add(connect,user)
            await connect.commit()
            
            return reg_user





