from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles 
from pathlib import Path

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    data = {"message": "Pagina de inicio del proyecto pagina web de peliculas."}

    return templates.TemplateResponse("main_template.html", {"request": request, "data": data})

@app.get("/cortes")
def read_root(request: Request, nombre:str=None):
    if nombre == None:
        data = {"message": f"No recibi informacion de la variable"}
    else:        
        data = {"message": f"{nombre}"}

    return templates.TemplateResponse("main_cortes.html", {"request": request, "data": data})

@app.get("/multiplicar2")
def multiplicar2(number:int):
    return number*2
