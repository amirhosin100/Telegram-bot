import asyncio
from config import settings
from aiogram import Bot, Dispatcher



bot = Bot(token=settings.TELEGRAM_TOKEN)
dp = Dispatcher()


@dp.message()
async def main_message(message):
    await message.answer("hello")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

