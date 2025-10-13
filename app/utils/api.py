from fastapi import APIRouter, FastAPI

api_router = APIRouter(prefix="/api")

# api_router.include_router(telegram_router)

def register_routes(app: FastAPI):
    app.include_router(api_router)