# 🤖 AI Text Styler Telegram Bot

Telegram-бот, який переписує текст користувача у різних стилях за допомогою AI (Google Vertex AI / Gemini).

---

## 🚀 Функціонал

- Переписує текст у різних стилях:
  - 🌆 Кіберпанк
  - ⚔️ Вікінг
  - 🤖 Саркастичний робот
  - 💼 Діловий стиль
  - 😂 Мемний стиль
- Зручний вибір стилю через кнопки
- Можливість змінювати стиль у будь-який момент
- Динамічна генерація тексту за допомогою AI

---

## 🧠 Як це працює

1. Користувач відкриває чат із ботом
2. Натискає кнопку **Start** або вводить `/start`
3. Обирає стиль через кнопки
4. Надсилає текст
5. Бот обробляє текст через AI
6. Повертає результат у вибраному стилі

---
## 🛠️ Технології

- Python
- aiogram (Telegram Bot API)
- Google Vertex AI (Gemini)
- python-dotenv

---

## ⚙️ Встановлення

1. Клонувати репозиторій:
`git clone https://github.com/OlenaDovh/Integration-with-AI-models.git`

2. Створити віртуальне середовище:
python -m venv .venv
3. Активувати середовище:

.venv\Scripts\activate


4. Встановити залежності:

pip install aiogram python-dotenv google-genai


---

## 🔑 Налаштування

Створи файл `.env`:


BOT_TOKEN=your_telegram_bot_token
GOOGLE_CLOUD_PROJECT=your_project_id
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_APPLICATION_CREDENTIALS=credentials/vertex-key.json


---

## ▶️ Запуск


python main.py


---

## 💡 Приклад використання

1. Натисни `/start`
2. Обери стиль
3. Надішли текст:


Я сьогодні дуже втомився


4. Отримаєш відповідь у вибраному стилі

---

## 🔒 Безпека

- `.env` і `credentials/` не додаються в репозиторій
- Секретні ключі не зберігаються у відкритому вигляді

---

## 📌 Примітка

Для роботи необхідно:
- активний Google Cloud проект
- увімкнений Vertex AI API
- service account JSON ключ
- підключений billing (можна free trial)

---

## 🎯 Мета проєкту

- інтеграція AI у застосунок
- робота з API
- побудова структури проєкту
- обробка користувацьких запитів

---