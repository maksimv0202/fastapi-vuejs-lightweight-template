from fastapi import APIRouter

from . import router


api_router = APIRouter()

# Include your routers here
api_router.include_router(router=router.example_router, tags=['example_router'])
