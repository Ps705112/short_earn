import os
from pyrogram import Client

bot = Client(
    "my-mdisk",
    api_id="8742500",
    api_hash="7ff1dec1b54f5e90d31d633a7729ad7b",
    bot_token="5310573576:AAEacytEzyH-Mr087HiSjLEgdvYrVYlFtOQ",
)

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")