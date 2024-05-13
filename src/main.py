from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config import settings

app = FastAPI()



@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <a href="http://127.0.0.1:8000/docs">Documentation</a><br>
    <a href="http://127.0.0.1:8000/redoc">ReDoc</a>
    """

print(settings.POSTGRES_DB)