from fastapi import FastAPI
from .routes import router  # tener router definido

app = FastAPI()

app.include_router(router)