from fastapi import APIRouter

from app.routes.api.v1 import api_v1_routers


api_routers = APIRouter()


api_routers.include_router(router=api_v1_routers, prefix="/v1")