from asyncio import run
from pyrogram import Client
from config_api.config import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_BOT_TOKEN

app = Client(
    "WeatherCast01Bot",
    api_id=TELEGRAM_API_ID,
    api_hash=TELEGRAM_API_HASH,
    bot_token=TELEGRAM_BOT_TOKEN
)


async def main():
    await app.start()
    await app.send_message(
        'WeatherCast', 'Olá'
    )
    await app.stop()


run(main())
