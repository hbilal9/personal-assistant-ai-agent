from fastapi import Request, Response
from http import HTTPStatus
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from config import settings
from app.features.agent.service import chat_handler

app_bot = (
    Application.builder()
    .token(settings.TELEGRAM_BOT_TOKEN)
    .build()
)

async def initialize_telegram_bot():
    await app_bot.bot.setWebhook(settings.WEBHOOK_URL)
    await app_bot.initialize()
    await app_bot.start()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Bot is running.")

async def process_update(request: Request):
    json_update = await request.json()
    update = Update.de_json(json_update, app_bot.bot)
    await app_bot.process_update(update)
    return Response(status_code=HTTPStatus.OK)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    print("User text: ", user_text)
    response = await chat_handler(user_text)
    await update.message.reply_text(response)

app_bot.add_handler(CommandHandler("start", start))
app_bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))