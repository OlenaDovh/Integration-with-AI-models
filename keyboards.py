from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_style_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🌆 Кіберпанк", callback_data="style:cyberpunk"),
                InlineKeyboardButton(text="⚔️ Вікінг", callback_data="style:viking")
            ],
            [
                InlineKeyboardButton(text="🤖 Робот", callback_data="style:robot"),
                InlineKeyboardButton(text="💼 Діловий", callback_data="style:business")
            ],
            [
                InlineKeyboardButton(text="😂 Мемний", callback_data="style:meme")
            ]
        ]
    )


def get_main_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🎨 Обрати стиль", callback_data="choose_style")
            ]
        ]
    )