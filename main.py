import os
import re
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import threading
from flask import Flask

# --- Détection automatique du TOKEN ---
BOT_TOKEN = None
# 1. Cherche les noms classiques
for name in ["BOT_TOKEN", "TELEGRAM_TOKEN", "TOKEN", "TOK", "TELEGRAM_BOT_TOKEN"]:
    if os.getenv(name):
        BOT_TOKEN = os.getenv(name)
        break

# 2. Si pas trouvé, cherche n'importe quelle variable qui ressemble à un token (chiffres:lettres)
if not BOT_TOKEN:
    for k, v in os.environ.items():
        if v and ":" in v and len(v) > 30 and re.match(r"^\d+:[A-Za-z0-9_-]+$", v.strip()):
            BOT_TOKEN = v.strip()
            print(f"Token trouvé dans la variable {k}")
            break

# 3. Chat ID (optionnel)
CHAT_ID = os.getenv("CHAT_ID") or os.getenv("CHAT") or ""
for k,v in os.environ.items():
    if k.startswith("CHA") and v:
        CHAT_ID = v
        break

print(f"TOKEN trouvé: {'OUI' if BOT_TOKEN else 'NON'}")
print(f"CHAT_ID trouvé: {CHAT_ID}")

# --- Flask pour garder Render en vie ---
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot N-oTrade-ia en ligne !"

# --- Commandes Telegram ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Salut Pascal ! Bot N-oTrade-ia est EN LIGNE et prêt ! Tape /status")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"✅ Bot OK\nTOKEN: {'OK' if BOT_TOKEN else 'MANQUANT'}\nCHAT_ID: {CHAT_ID}")

if __name__ == "__main__":
    if not BOT_TOKEN:
        print("ERREUR: Aucun token trouvé !")
    else:
        # Lancer Flask en arrière plan
        threading.Thread(target=lambda: app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000))), daemon=True).start()
        # Lancer le bot Telegram
        app_bot = ApplicationBuilder().token(BOT_TOKEN.strip()).build()
        app_bot.add_handler(CommandHandler("start", start))
        app_bot.add_handler(CommandHandler("status", status))
        print("Bot démarré en polling...")
        app_bot.run_polling()
