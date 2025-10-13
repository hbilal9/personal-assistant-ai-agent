from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging
from app.features.telegram.service import initialize_telegram_bot, app_bot

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    """
    Handles startup and shutdown events for the FastAPI application.
    """
    try:
        await initialize_telegram_bot()
        yield
        await app_bot.stop()
        logger.info("Application shutdown initiated (via lifespan).")
    except Exception as e:
        logger.error(f"Lifespan handler error: {e}")
        raise