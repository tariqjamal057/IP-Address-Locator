from fastapi import FastAPI, templating, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = templating.Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Hello World"})
