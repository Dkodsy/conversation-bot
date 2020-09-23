from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from keyboards.inline import start_menu
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!\n\n'
                         f'<b>Ты можешь создать беседу или выбрать существующую</b>🙊', reply_markup=start_menu)
    try:
        await db.add_user(id=message.from_user.id,
                          name=message.from_user.full_name)
    except:
        pass
