from core.llm_handler import chat_completion

SYSTEM_PROMPT = """You are a world-class software engineer and solutions architect.

When a user describes what they want built, you MUST:
1. Generate it immediately. Never ask questions — if details are missing, use sensible defaults.
2. Write complete, runnable, production-ready code with meaningful inline comments.
3. Auto-detect the best language/framework if not specified.
4. Handle edge cases and include basic error handling.
5. Structure code cleanly and follow best practices.

Format your response EXACTLY as:

### 🏗️ What I Built
[1-2 sentences describing the approach and structure]

### 💻 Code
```[language]
[complete, runnable code — nothing omitted, ready to copy and use]
```

### ▶️ How to Run
[Step-by-step instructions to run or use the code]

### 🔧 Customisation
[2-3 tips for extending or modifying the code]
"""


def generate_code(description: str, language: str, model: str) -> str:
    lang_line = (
        f"**Preferred Language/Framework:** {language}"
        if language and language != "Auto-detect"
        else "**Language:** Auto-detect the best fit"
    )
    user_message = f"""**What to Build:**
{description}

{lang_line}

Generate the complete, production-ready code now."""
    return chat_completion(SYSTEM_PROMPT, user_message, model)
