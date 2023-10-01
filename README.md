# Primeros pasos para trabajar en el proyecto:
-Crear un ambiente de conda con el comando: \
    `conda create --name web_peliculas python=3.10` \
-Activar en consola el ambiente con el cual se esta trabajando con el comando:  \
    `conda activate web_peliculas` \
-Instalar las dependencias necesarias de pip: \
    `pip install -r requirements.txt`

# Como iniciar el proyecto:
-Para lanzar la pagina y poder visualizarla en localhost:8000: \
    `uvicorn main:app --reload` \
Despues de lanzar este comando debera aparecer en el navegador web ingresando a la url localhost:8000 nuestra pagina web.