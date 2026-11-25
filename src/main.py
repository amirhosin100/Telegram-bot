import asyncio
from config import settings
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart



bot = Bot(token=settings.TELEGRAM_TOKEN)
dp = Dispatcher()


@dp.message()
async def main_message(message):
    await message.answer("hello")

@dp.message(CommandStart())
async def start_message(message):
    await message.answer("Hi I am amirhossein bot. If you'er AmirHossein, I'll do anything you need")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

