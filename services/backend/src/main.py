from fastapi import FastAPI

from .routers import api


app = FastAPI()

app.include_router(router=api.api_router, tags=['api'])
