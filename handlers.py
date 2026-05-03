from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from ai_service import generate_text
from keyboards import get_style_keyboard, get_main_keyboard


router = Router()

style_names = {
    "cyberpunk": "Кіберпанк",
    "viking": "Вікінг",
    "robot": "Саркастичний робот",
    "business": "Діловий стиль",
    "meme": "Мемний стиль"
}

user_styles = {}


@router.message(CommandStart())
async def start_handler(message: Message):
    text = """
Привіт! Я AI-Стилізатор повідомлень.

Спочатку обери стиль, а потім надішли текст, який потрібно переписати.
"""
    await message.answer(text, reply_markup=get_style_keyboard())


@router.message(Command("style"))
async def style_handler(message: Message):
    await message.answer("Обери стиль:", reply_markup=get_style_keyboard())


@router.message(Command("help"))
async def help_handler(message: Message):
    text = """
Як користуватися ботом:

1. Натисни /start або /style
2. Обери стиль кнопкою
3. Надішли текст
4. Бот перепише його у вибраному стилі

Щоб змінити стиль, натисни кнопку “🎨 Обрати стиль” або команду /style.
"""
    await message.answer(text)


@router.callback_query(F.data.startswith("style:"))
async def style_callback(callback: CallbackQuery):
    style = callback.data.split(":")[1]
    user_styles[callback.from_user.id] = style

    await callback.message.answer(
        f"Стиль обрано: {style_names[style]}\nТепер надішли текст, який потрібно обробити.",
        reply_markup=get_main_keyboard()
    )
    await callback.answer()


@router.callback_query(F.data == "choose_style")
async def choose_style_callback(callback: CallbackQuery):
    await callback.message.answer(
        "Обери стиль:",
        reply_markup=get_style_keyboard()
    )
    await callback.answer()


@router.message()
async def text_handler(message: Message):
    user_id = message.from_user.id

    if user_id not in user_styles:
        await message.answer("Спочатку обери стиль:", reply_markup=get_style_keyboard())
        return

    style = user_styles[user_id]
    user_text = message.text.strip()

    if not user_text:
        await message.answer("Надішли текст, який потрібно обробити.")
        return

    await message.answer("Обробляю текст...")

    try:
        result = await generate_text(style, user_text)
        await message.answer(result, reply_markup=get_main_keyboard())
    except Exception as e:
        await message.answer(f"Помилка: {e}")