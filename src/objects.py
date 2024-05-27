from sqlalchemy import insert, values, delete
from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"])

class AuthService:
    @staticmethod
    def get_password_hash(password:str):
        return context.hash(password)
    
    @staticmethod

