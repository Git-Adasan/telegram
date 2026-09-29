import asyncio
from telethon import TelegramClient

API_ID   = 39800053
API_HASH = "a3a2bbca1de2d161a87ee344c4bb9b88"

async def main():
    async with TelegramClient("update_session", API_ID, API_HASH) as client:
        print("✅ Сессия создана:", await client.get_me())

asyncio.run(main())