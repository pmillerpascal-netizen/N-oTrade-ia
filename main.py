import os
import logging
from threading import Thread
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask pour Render
app_flask = Flask(__name__)
@app_flask.route('/')
def home():
    return "Bot N-oTrade IA Actif!"

# Trouve le token
TOKEN = None
for k, v in os.environ.items():
    if "TOK" in k.upper() or "BOT" in k.upper():
        if v and ":" in v:
            TOKEN = v.strip()
            break
if not TOKEN:
    TOKEN = os.getenv("BOT_TOKEN") or os.getenv("TELEGRAM_TOKEN")

print(f"TOKEN trouvé: {'OUI' if TOKEN else 'NON'}")

# Commandes
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Salut Pascal ! Bot N-oTrade IA est enfin en ligne !\nTape /help")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commandes:\n/start - Démarrer\n/help - Aide\nEnvoie un message pour tester.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Tu as dit: {update.message.text}")

def run_bot():
    if not TOKEN:
        print("ERREUR: Token non trouvé!")
        return
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_cmd))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot démarré en polling...")
    application.run_polling()

if __name__ == "__main__":
    Thread(target=lambda: app_flask.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))).start()
    run_bot()
