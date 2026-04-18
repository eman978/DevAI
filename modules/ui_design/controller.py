from modules.ui_design.service import generate_ui


def handle_ui_request(idea: str, model: str) -> dict:
    if not idea.strip():
        return {"success": False, "result": "", "error": "Please describe what UI you want to generate."}
    try:
        result = generate_ui(idea, model)
        return {"success": True, "result": result, "error": ""}
    except RuntimeError as exc:
        return {"success": False, "result": "", "error": str(exc)}
