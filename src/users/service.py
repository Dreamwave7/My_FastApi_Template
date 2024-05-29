from sqlalchemy import insert, values, delete
from passlib.context import CryptContext
from users import schemas
from database import Session
from models import UserModel

context = CryptContext(schemes=["bcrypt"])

class UserService:
    @staticmethod
    async def register_new_user(user: schemas.UserRegister):
        async with Session() as connect:
            new_user = UserModel(**user.model_dump())
            adding = connect.add(new_user)
            await connect.commit()
            return "done"





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

    

