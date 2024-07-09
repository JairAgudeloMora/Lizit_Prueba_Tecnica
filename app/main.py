from fastapi import FastAPI
from app.routers import items_router

app = FastAPI()

app.include_router(items_router)
