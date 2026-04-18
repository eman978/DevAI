from groq import Groq
import os
from core.config import MAX_TOKENS, TEMPERATURE


def chat_completion(system_prompt: str, user_message: str, model: str) -> str:
    api_key = os.environ.get("GROQ_API_KEY", "")
    
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Please add it to your .env file or environment variables."
        )

    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
    )

    return response.choices[0].message.content
