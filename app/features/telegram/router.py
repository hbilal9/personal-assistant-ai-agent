from fastapi import APIRouter, Request
from .service import process_update

router = APIRouter(prefix="/telegram")

@router.post("/webhook")
async def webhook(request: Request):
    await process_update(request)
    return {"message": "Webhook received"}
    