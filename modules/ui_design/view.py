"""
UI Design Assistant — View layer.
Input and output on the SAME page — no tab switching needed.
"""

import streamlit as st
from modules.ui_design.controller import handle_ui_request
from utils.helpers import extract_first_code_block


def render(model: str) -> None:
    st.markdown("## 🔵 UI Design Assistant")
    st.markdown(
        "Describe any UI you want — a login page, dashboard, logo, form, navbar, anything. "
        "The AI will generate the complete code right away."
    )
    st.markdown("---")

    # ── Input section ──────────────────────────────────────────────
    idea = st.text_area(
        "What do you want to build?",
        height=200,
        placeholder=(
            "Examples:\n"
            "• Generate a logo for my name 'Ali' in blue and white\n"
            "• A dark mode login page with email and password fields\n"
            "• A responsive navbar with Home, About, Contact links\n"
            "• An admin dashboard with sidebar and KPI cards\n"
            "• A contact form with name, email, message fields"
        ),
        key="ui_idea",
    )

    generate_clicked = st.button("🎨 Generate UI", type="primary", use_container_width=True)

    # ── Output section — shown on same page ────────────────────────
    if generate_clicked:
        if not idea.strip():
            st.error("⚠️ Please describe what you want to build above.")
        else:
            with st.spinner("Generating your UI…"):
                response = handle_ui_request(idea, model)

            if response["success"]:
                st.success("✅ UI generated!")
                st.markdown("---")
                st.markdown(response["result"])

                st.markdown("---")
                with st.expander("📋 Code — Copy Ready", expanded=True):
                    ui_code = extract_first_code_block(response["result"])
                    st.code(ui_code, language="html")
            else:
                st.error(f"❌ {response['error']}")
