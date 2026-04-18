from modules.code_generate.service import generate_code


def handle_generate_request(description: str, language: str, model: str) -> dict:
    if not description.strip():
        return {"success": False, "result": "", "error": "Please describe what you want to build."}
    try:
        result = generate_code(description, language, model)
        return {"success": True, "result": result, "error": ""}
    except RuntimeError as exc:
        return {"success": False, "result": "", "error": str(exc)}
