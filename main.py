import os
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio
import threading

app = Flask(__name__)

TOKEN = os.environ.get("BOT_TOKEN") or os.environ.get("TELEGRAM_TOKEN") or ""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Salut Pascal ! N-oTrade IA est EN LIGNE !\n\n"
        "Commandes:\n"
        "/start - Démarrer\n"
        "/help - Aide\n"
        "/status - Statut du bot"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Je suis ton bot de trading IA. Je suis live 24/7 sur Render !")

async def status_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot opérationnel ! Hébergé sur Render.")

def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_cmd))
    application.add_handler(CommandHandler("status", status_cmd))
    print("Bot démarré...")
    loop.run_until_complete(application.run_polling())

@app.route('/')
def home():
    return "N-oTrade IA is Live! Bot running."

# Lancer le bot dans un thread
if TOKEN:
    threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
