from google import genai
from settings import GOOGLE_CLOUD_PROJECT, GOOGLE_CLOUD_LOCATION, credentials

client = genai.Client(
    vertexai=True,
    project=GOOGLE_CLOUD_PROJECT,
    location=GOOGLE_CLOUD_LOCATION,
    credentials=credentials
)


styles = {
    "cyberpunk": "Перепиши текст у стилі кіберпанк. Відповідь має бути короткою, атмосферною і трохи футуристичною.",
    "viking": "Перепиши текст у стилі вікінга. Відповідь має звучати сміливо, епічно і просто.",
    "robot": "Перепиши текст у стилі саркастичного робота з майбутнього. Використовуй технічні терміни, трохи іронії та звертайся до людини як до органічної істоти. Відповідь має бути короткою і дотепною.",
    "business": "Перепиши текст у діловому стилі. Відповідь має бути ввічливою, зрозумілою і професійною.",
    "meme": "Перепиши текст у мемному стилі. Відповідь має бути смішною, простою і сучасною."
}


async def generate_text(style: str, user_text: str) -> str:
    """Генерує текст у заданому стилі за допомогою Gemini.

    Args:
        style: Назва стилю генерації тексту.
        user_text: Вхідний текст користувача.

    Returns:
        Згенерований текст.
    """

    prompt = f"{styles[style]}\n\nТекст: {user_text}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text