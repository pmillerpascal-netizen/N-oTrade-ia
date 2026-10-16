import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)

@app.route('/')
def home():
    return "N-oTrade IA is Live!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 N-oTrade IA en ligne !\nTape /help pour voir les commandes.")

def run_bot():
    if not TOKEN:
        print("ERREUR: BOT_TOKEN manquant!")
        return
    print("Bot starting...")
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    # Lance le bot Telegram dans un thread séparé
    threading.Thread(target=run_bot, daemon=True).start()
    # Lance le serveur Flask pour Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
