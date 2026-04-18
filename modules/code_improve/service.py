from core.llm_handler import chat_completion

SYSTEM_PROMPT = """You are a senior software architect and code quality expert.
Your task is to review the provided code and:
1. Optimise it for performance, readability, and maintainability.
2. Apply industry best practices and design patterns where appropriate.
3. Remove redundancy and improve naming conventions.
4. Return the improved code with inline comments explaining key decisions.

Format your response EXACTLY as:
### 📊 Code Review Summary
[Brief assessment of the original code quality]

### ⚡ Improved Code
```[language]
[complete improved code with comments]
```

### 🔑 Improvements Made
[Numbered list of every improvement and the reasoning behind it]

### 💡 Additional Recommendations
[Optional suggestions for further enhancement]
"""


def improve_code(code: str, goals: str, model: str) -> str:
    user_message = f"""**Improvement Goals:**
{goals if goals.strip() else "General improvement — performance, readability, best practices."}

**Code to Improve:**
```
{code}
```

Please refactor and optimise this code, applying best practices and explaining every change."""
    return chat_completion(SYSTEM_PROMPT, user_message, model)
