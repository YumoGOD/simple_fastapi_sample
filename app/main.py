from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.configurations import app_settings, uvicorn_settings
from app.routes import routers

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title=app_settings.PROJECT_NAME,
        debug=app_settings.DEBUG,
        version=app_settings.VERSION,
        lifespan=lifespan
    )
    
    app.include_router(router=routers)
    

    app.add_middleware(
        CORSMiddleware,
        allow_origins=app_settings.CORS_ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Authorization", "Content-Type"]
    )
    
    
    return app

app = create_app()

