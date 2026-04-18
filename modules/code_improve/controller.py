from modules.code_improve.service import improve_code


def handle_improve_request(code: str, goals: str, model: str) -> dict:
    if not code.strip():
        return {"success": False, "result": "", "error": "Please paste the code you want to improve."}
    try:
        result = improve_code(code, goals, model)
        return {"success": True, "result": result, "error": ""}
    except RuntimeError as exc:
        return {"success": False, "result": "", "error": str(exc)}
