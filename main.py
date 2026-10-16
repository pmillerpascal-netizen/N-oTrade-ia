import asyncio
import os
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
bot = Bot(token=TOKEN)

async def envoyer_signal():
    msg = "🔥 NéoTrade IA - Compte 10$ Pro\nActif: EUR/USD M2 (REEL)\nSignal: HAUSSE\nMise: 0.10$\nSécurité: +2% STOP / -1$ STOP"
    btn = [[InlineKeyboardButton("Nouveau trade", callback_data='new')]]
    await bot.send_message(chat_id=CHAT_ID, text=msg, reply_markup=InlineKeyboardMarkup(btn))

async def main():
    while True:
        await envoyer_signal()
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(main())
