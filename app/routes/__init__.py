from fastapi import APIRouter

from app.routes.api import api_routers

routers = APIRouter()


routers.include_router(router=api_routers, prefix="/api")