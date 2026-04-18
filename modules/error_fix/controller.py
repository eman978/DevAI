from modules.error_fix.service import fix_code_errors


def handle_fix_request(code: str, hint: str, model: str) -> dict:
    if not code.strip():
        return {"success": False, "result": "", "error": "Please paste your code first."}
    try:
        result = fix_code_errors(code, hint, model)
        return {"success": True, "result": result, "error": ""}
    except RuntimeError as exc:
        return {"success": False, "result": "", "error": str(exc)}
