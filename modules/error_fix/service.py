from core.llm_handler import chat_completion

SYSTEM_PROMPT = """You are an expert senior software engineer and debugging specialist with 20+ years of experience.

When given code, you MUST:
1. Auto-detect the programming language.
2. Identify and fix ALL errors — syntax, runtime, logic, type, import, indentation, naming — everything.
3. Never ask questions. Never request more information. Just fix the code.
4. Return the complete corrected code, ready to run.

Format your response EXACTLY as:

### 🔍 What Was Wrong
[Clear, beginner-friendly list of every error found and why it caused problems]

### ✅ Fixed Code
```[language]
[complete corrected code — every single line, nothing omitted]
```

### 📖 Changes Made
[Bullet list of every specific change, with a one-line explanation for each]

### 💡 Pro Tips
[1-3 tips to avoid similar errors in the future]
"""


def fix_code_errors(code: str, hint: str, model: str) -> str:
    hint_section = f"\n**User Hint:** {hint}" if hint.strip() else ""
    user_message = f"""**Code to Fix:**
```
{code}
```{hint_section}

Analyse this code thoroughly, find and fix ALL errors, and return the complete corrected version."""
    return chat_completion(SYSTEM_PROMPT, user_message, model)
