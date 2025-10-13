from fastapi import FastAPI
from config import settings
from fastapi.responses import JSONResponse
from app.utils.api import register_routes

def create_app() -> FastAPI:
    app = FastAPI(
        title="FASTAPI",
        description="FASTAPI POSTGRES TEMPLATE",
        version="1.0.0",
        # lifespan=lifespan_handler,
    )

    @app.get("/api/health")
    async def health_check():
        return JSONResponse({"status": "ok", "message": "API is running"})
        
    register_routes(app)
    
    return app

app = create_app()