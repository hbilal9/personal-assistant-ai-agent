from fastapi import FastAPI
from contextlib import asynccontextmanager
from config import settings
import logging
from app.features.telegram.service import app_bot

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan_handler(app: FastAPI):
    """
    Handles startup and shutdown events for the FastAPI application.
    """
    try:
        await app_bot.bot.setWebhook(settings.WEBHOOK_URL)
        async with app_bot:
            await app_bot.start()
            yield
            await app_bot.stop()
        logger.info("Application shutdown initiated (via lifespan).")
    except Exception as e:
        logger.error(f"Lifespan handler error: {e}")
        raise