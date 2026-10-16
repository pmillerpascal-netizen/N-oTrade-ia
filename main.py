import asyncio
import os
import threading
from flask import Flask
from telegram import Bot

TOKEN = os.environ.get("TOKEN") or os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID") or os.environ.get("CHANNEL_ID")

app = Flask(__name__)

@app.route('/')
def home():
    return "N-oTrade IA is Running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

bot = Bot(token=TOKEN)

async def envoyer_signal():
    msg = "🔥 N-oTrade IA - Signal OK, bot demarre!"
    await bot.send_message(chat_id=CHAT_ID, text=msg)
    print("Signal envoye")

async def main():
    print("Bot N-oTrade IA demarre...")
    await envoyer_signal()
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    threading.Thread(target=run_web).start()
    asyncio.run(main())
