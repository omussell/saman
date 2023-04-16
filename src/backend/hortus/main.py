from typing import Optional

from fastapi import FastAPI
from fastapi.responses import FileResponse

from image.generation import generate_image

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    img = generate_image()
    #return FileResponse("my_image.png")
    #return FileResponse("my_other_image.png")
    return FileResponse("example1.svg")

@app.get("/images", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("image.html", {"request": request})


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}