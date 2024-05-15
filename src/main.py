from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from database import get_session

app = FastAPI()



@app.get("/", response_class=HTMLResponse)
async def home(db = Depends(get_session)):

    
    return """
    <a href="http://127.0.0.1:8000/docs">Documentation</a><br>
    <a href="http://127.0.0.1:8000/redoc">ReDoc</a>
    """

