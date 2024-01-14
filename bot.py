import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import Config


router = Router(name=__name__)


async def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(text='🍎 Click me!',
                   web_app=WebAppInfo(
                       url='https://example.com'
                   ))

    return builder.as_markup()


@router.message(CommandStart())
async def cmd_start(message: Message):
    mention = message.from_user.mention_html(message.from_user.first_name)
    markup = await webapp_builder()

    await message.answer(f'Hello, {mention}', reply_markup=markup)


async def main():
    bot = Bot(Config.TOKEN, parse_mode=ParseMode.HTML)

    dp = Dispatcher()
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
