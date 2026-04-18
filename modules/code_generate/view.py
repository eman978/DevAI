"""
Code Generate — View layer.
Input and output on the SAME page — no tab switching needed.
"""

import streamlit as st
from modules.code_generate.controller import handle_generate_request
from utils.helpers import extract_first_code_block, detect_language

LANGUAGES = [
    "Auto-detect (AI chooses best fit)",
    "Python",
    "JavaScript / Node.js",
    "TypeScript",
    "React (JSX/TSX)",
    "HTML + CSS + JS",
    "Java",
    "C++",
    "C#",
    "Go",
    "Rust",
    "PHP",
    "SQL",
    "Bash / Shell",
    "Kotlin",
    "Swift",
    "Other (describe in your request)",
]


def render(model: str) -> None:
    st.markdown("## 🟢 Generate Code")
    st.markdown(
        "Describe what you want to build and click **Generate**. "
        "The AI will produce complete, ready-to-run code — no follow-up questions."
    )
    st.markdown("---")

    # ── Input section ──────────────────────────────────────────────
    description = st.text_area(
        "What do you want to build?",
        height=220,
        placeholder=(
            "Examples:\n"
            "• A Python web scraper that fetches product prices\n"
            "• A REST API in Node.js for a todo list with CRUD operations\n"
            "• A login page with HTML, CSS and JavaScript validation\n"
            "• A binary search tree in Java with insert, delete, and search"
        ),
        key="gen_description",
    )

    language = st.selectbox(
        "Preferred language / framework (optional — AI picks if left on Auto)",
        LANGUAGES,
        key="gen_language",
    )

    generate_clicked = st.button("🚀 Generate Code", type="primary", use_container_width=True)

    # ── Output section — shown on same page ────────────────────────
    if generate_clicked:
        if not description.strip():
            st.error("⚠️ Please describe what you want to build above.")
        else:
            lang_choice = "" if language.startswith("Auto") else language
            with st.spinner("Generating your code…"):
                response = handle_generate_request(description, lang_choice, model)

            if response["success"]:
                st.success("✅ Code generated!")
                st.markdown("---")
                st.markdown(response["result"])

                st.markdown("---")
                with st.expander("📋 Code — Copy Ready", expanded=True):
                    generated = extract_first_code_block(response["result"])
                    lang      = detect_language(generated)
                    st.code(generated, language=lang)
            else:
                st.error(f"❌ {response['error']}")
