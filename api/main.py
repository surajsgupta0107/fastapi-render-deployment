# Eric Roby - https://www.youtube.com/watch?v=p7caQ1Cvl6Y

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .middleware import configure_middleware
from .api import register_routes
from .database.core import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

configure_middleware(app)

templates = Jinja2Templates(directory="templates")


@app.get("/healthy")
def health_check():
    return "Health check complete"


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


register_routes(app)
