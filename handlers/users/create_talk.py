from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import talk_callback
from loader import dp, db
from states.talk_states import Talk


@dp.callback_query_handler(talk_callback.filter(action="choose_talk"))
async def choose_create(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Выберите беседу")


@dp.callback_query_handler(talk_callback.filter(action="create_talk"))
async def choose_create(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer("Введите название вашей беседы", reply_markup=None)
    await Talk.S1.set()


@dp.message_handler(state=Talk.S1)
async def answer_S1(message: types.Message, state: FSMContext):
    name_talk = message.text
    await message.answer(f"Вы назвали беседу {name_talk}")
    await db.add_talk(talk=name_talk, id=message.from_user.id)
    await state.finish()
