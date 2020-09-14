from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import talk_callback

start_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Создать новый разговорчик", callback_data=talk_callback.new("create_talk")),

    ],
    [
        InlineKeyboardButton(text="Добавить тему обсуждения в разговорчик",
                             callback_data=talk_callback.new("add_talk"))
    ],
    [
        InlineKeyboardButton(text="Отмена",
                             callback_data=talk_callback.new("cancel"))
    ]
],
)
