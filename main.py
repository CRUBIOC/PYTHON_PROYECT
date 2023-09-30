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
    data = {"message": "Página de inicio del proyecto página web de películas."}

    return templates.TemplateResponse(
        "main_template.html", {"request": request, "data": data}
    )


@app.get("/JuanD")
def Test_JuanD(request: Request):
    data = {"message": "Se hace lo que se puede"}

    return templates.TemplateResponse("Prueba.html", {"request": request, "data": data})
