from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import talk_callback

start_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Выбрать беседу", callback_data=talk_callback.new("choose_talk")),
        InlineKeyboardButton(text="Создать", callback_data=talk_callback.new("create_talk"))
    ],
    [
        InlineKeyboardButton(text="Отмена",
                             callback_data=talk_callback.new("cancel"))
    ]
],
)
