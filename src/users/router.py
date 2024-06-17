from fastapi import APIRouter, Request, Response, Depends
from users.schemas import UserLogin, UserRegister
from users.service import UserService, AuthService
from fastapi.security import OAuth2PasswordRequestForm
from exceptions import InvalidLoginExceptions

user_router = APIRouter(prefix="/auth")

@user_router.post("/register")
async def register(user_data : UserRegister):
    result = await UserService.register_new_user(user_data)
    return result 

@user_router.post("/login")
async def login(response:Response, user_data = Depends(OAuth2PasswordRequestForm)):
    checker_user = await AuthService.check_user(user_data.username, user_data.password)
    if not checker_user:
        raise InvalidLoginExceptions
    access_token = await AuthService.create_access_token(user_data.username)

    response.set_cookie("access_token", access_token, max_age=10000)
    return access_token


@user_router.get("/delete")
async def delete_user(request: Request):
    pass


@user_router.get("/logout")
async def logout_user(response:Response):
    response.delete_cookie("access_token")
    return "User logged out"


# @user_router.get("/login")
# async def login(response:Response, email:str, password:str):
#     checker_user = await AuthService.check_user(email, password)
#     if not checker_user:
#         raise InvalidLoginExceptions
#     access_token = await AuthService.create_access_token(email)

#     response.set_cookie("access_token", access_token, max_age=260000)
#     return access_token




@user_router.get("/who_iam")
async def check_cookie(request:Request):
    token = request.cookies.get("access_token")
    if token:
        return token
    return "User not logged"