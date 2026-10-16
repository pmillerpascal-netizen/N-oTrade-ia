import asyncio
import os
from telegram import Bot

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

bot = Bot(token=TOKEN)

async def envoyer_signal():
    msg = "🔥 N-oTrade IA - Signal\n\n💰 Compte 10$ prêt\n📈 Analyse en cours...\n✅ Bot connecté avec succès !"
    await bot.send_message(chat_id=CHAT_ID, text=msg)
    print("Signal envoyé")

async def main():
    print("Bot N-oTrade IA démarré...")
    await envoyer_signal()
    while True:
        await asyncio.sleep(3600)
        await envoyer_signal()

if __name__ == '__main__':
    asyncio.run(main())
