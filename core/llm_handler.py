"""
LLM Handler — Groq API wrapper.
"""

from groq import Groq
from core.config import GROQ_API_KEY, MAX_TOKENS, TEMPERATURE


def chat_completion(system_prompt: str, user_message: str, model: str) -> str:
    if not GROQ_API_KEY:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Please add it to your .env file or environment variables."
        )

    client = Groq(api_key=GROQ_API_KEY)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_message},
        ],
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
    )

    return response.choices[0].message.content
