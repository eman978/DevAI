import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")

AVAILABLE_MODELS = {
    "llama-3.3-70b-versatile": "Llama 3.3 70B — Best for complex tasks",
    "llama-3.1-8b-instant":    "Llama 3.1 8B — Fast & lightweight",
    "mixtral-8x7b-32768":      "Mixtral 8x7B — Long context (32k tokens)",
    "gemma2-9b-it":            "Gemma 2 9B — Instruction tuned",
}

DEFAULT_MODEL  = "llama-3.3-70b-versatile"
MAX_TOKENS     = 4096
TEMPERATURE    = 0.3
APP_NAME       = "DevAI"
APP_SUBTITLE   = "Developer AI Code Assistant"
APP_VERSION    = "v1.0.0"
