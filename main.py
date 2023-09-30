from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    data = {"message": "Pagina de inicio del proyecto pagina web de peliculas."}

    return templates.TemplateResponse("main_template.html", {"request": request, "data": data})