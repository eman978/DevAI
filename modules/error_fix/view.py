"""
Error Fix — View layer.
Input and output on the SAME page — no tab switching needed.
"""

import streamlit as st
from modules.error_fix.controller import handle_fix_request
from utils.helpers import extract_first_code_block, detect_language


def render(model: str) -> None:
    st.markdown("## 🔴 Fix Errors")
    st.markdown(
        "Paste your broken code and click **Fix My Code**. "
        "The AI will automatically find and fix every error."
    )
    st.markdown("---")

    # ── Input section ──────────────────────────────────────────────
    code = st.text_area(
        "Paste your broken code here",
        height=280,
        placeholder="# Paste any broken code here — Python, JS, Java, C++, or any language…",
        key="error_fix_code",
    )

    hint = st.text_input(
        "Optional: Briefly describe what's going wrong",
        placeholder="e.g. 'crashes on line 5', 'infinite loop', 'wrong output' — or leave empty",
        key="error_fix_hint",
    )

    fix_clicked = st.button("🔧 Fix My Code", type="primary", use_container_width=True)

    # ── Output section — shown on same page ────────────────────────
    if fix_clicked:
        if not code.strip():
            st.error("⚠️ Please paste your code above first.")
        else:
            with st.spinner("Analysing and fixing all errors…"):
                response = handle_fix_request(code, hint, model)

            if response["success"]:
                st.success("✅ All errors fixed!")
                st.markdown("---")
                st.markdown(response["result"])

                st.markdown("---")
                with st.expander("📋 Fixed Code — Copy Ready", expanded=True):
                    fixed = extract_first_code_block(response["result"])
                    lang  = detect_language(fixed)
                    st.code(fixed, language=lang)
            else:
                st.error(f"❌ {response['error']}")
