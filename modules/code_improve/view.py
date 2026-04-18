"""
Code Improve — View layer.
Input and output on the SAME page — no tab switching needed.
"""

import streamlit as st
from modules.code_improve.controller import handle_improve_request
from utils.helpers import extract_first_code_block, detect_language


def render(model: str) -> None:
    st.markdown("## 🟡 Improve Code")
    st.markdown(
        "Paste your code and click **Improve**. "
        "The AI will refactor, optimise, and apply best practices — no extra input needed."
    )
    st.markdown("---")

    # ── Input section ──────────────────────────────────────────────
    code = st.text_area(
        "Paste your code here",
        height=280,
        placeholder="# Paste any working code here — Python, JS, Java, C++, or any language…",
        key="improve_code",
    )

    goals = st.text_input(
        "Optional: Specific improvement focus",
        placeholder="e.g. 'make it faster', 'add error handling', 'reduce complexity', 'add comments'",
        key="improve_goals",
    )

    improve_clicked = st.button("⚡ Improve Code", type="primary", use_container_width=True)

    # ── Output section — shown on same page ────────────────────────
    if improve_clicked:
        if not code.strip():
            st.error("⚠️ Please paste your code above first.")
        else:
            with st.spinner("Refactoring and optimising your code…"):
                response = handle_improve_request(code, goals, model)

            if response["success"]:
                st.success("✅ Code improved!")
                st.markdown("---")
                st.markdown(response["result"])

                st.markdown("---")
                with st.expander("📋 Improved Code — Copy Ready", expanded=True):
                    improved = extract_first_code_block(response["result"])
                    lang     = detect_language(improved)
                    st.code(improved, language=lang)
            else:
                st.error(f"❌ {response['error']}")
