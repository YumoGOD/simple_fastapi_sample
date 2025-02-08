from fastapi import APIRouter

from app.routes.api.v1.simple_api import router as simple_api_router

api_v1_routers = APIRouter()


api_v1_routers.include_router(router=simple_api_router)