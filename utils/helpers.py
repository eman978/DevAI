"""
Utility helpers shared across modules.
"""
import re


def extract_first_code_block(text: str) -> str:
    """Return the content of the first fenced code block found in *text*."""
    match = re.search(r"```(?:\w+)?\n(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else text.strip()


def detect_language(code: str) -> str:
    """Heuristically detect the language of a code snippet."""
    if re.search(r"^\s*(import|from|def |class |print\()", code, re.MULTILINE):
        return "python"
    if re.search(r"(const |let |var |=>|console\.log)", code):
        return "javascript"
    if re.search(r"(<html|<div|<body|<!DOCTYPE)", code, re.IGNORECASE):
        return "html"
    if re.search(r"(public\s+class|System\.out\.println)", code):
        return "java"
    if re.search(r"(#include|std::)", code):
        return "cpp"
    return "text"
