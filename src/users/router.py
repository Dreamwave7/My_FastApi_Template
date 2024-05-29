from fastapi import APIRouter
from users.schemas import UserRegister
from users.service import UserService

user_router = APIRouter(prefix="/auth")

@user_router.post("register")
async def register(user_data : UserRegister):
    result = await UserService.register_new_user(user_data)
    return result 