from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import talk_callback, theme_callback
from loader import dp, db
from states.talk_states import Talk


@dp.callback_query_handler(talk_callback.filter(action="choose_talk"))
async def choose_talk(call: CallbackQuery):
    await call.answer(cache_time=60)
    talks_list = await db.choose_talk(id=call.from_user.id)
    talks_keyboard = InlineKeyboardMarkup(row_width=6)

    for elem in talks_list:
        talks_keyboard.add(
            InlineKeyboardButton(text=elem['name_talk'],
                                 callback_data=theme_callback.new(action="conversation_selected",
                                                                  name=elem['name_talk'])))
    await call.message.answer("Выберите беседу", reply_markup=talks_keyboard)


@dp.callback_query_handler(theme_callback.filter(action="conversation_selected"))
async def list_of_themes(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    name_theme = callback_data.get("name")
    themes_list = await db.show_talk_themes(id=call.from_user.id, theme_name=name_theme)
    print(themes_list)


@dp.callback_query_handler(talk_callback.filter(action="create_talk"))
async def choose_create(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Введите название вашей беседы", reply_markup=None)
    await Talk.S1.set()


@dp.message_handler(state=Talk.S1)
async def answer_S1(message: types.Message, state: FSMContext):
    name_talk = message.text
    await message.answer(f"Вы назвали беседу {name_talk}")
    await db.add_talk(id=message.from_user.id, talk_name=name_talk)
    await state.finish()
