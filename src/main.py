from fastapi import FastAPI, Depends, Request, Response
from fastapi.responses import HTMLResponse
from database import get_session
from users.router import user_router
from users.service import UserService

app = FastAPI()
app.include_router(user_router)



@app.get("/", response_class=HTMLResponse)
async def home(response : Response, db = Depends(get_session)):
    response.set_cookie("testkey","testvalue")
    return """
    <a href="http://127.0.0.1:8000/docs">Documentation</a><br>
    <a href="http://127.0.0.1:8000/redoc">ReDoc</a>
    """


@app.get("/cookie")
async def get_cookie(request: Request):
    token = request.cookies.get("testkey")
    return token

    