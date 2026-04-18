"""
DevAI — Developer AI Code Assistant
Main entry point for the Streamlit application.

Run with:
    streamlit run main.py --server.port 5000
"""

import streamlit as st
from pathlib import Path

from core.config import AVAILABLE_MODELS, DEFAULT_MODEL, APP_NAME, APP_SUBTITLE, APP_VERSION
from modules.error_fix import view as error_fix_view
from modules.code_improve import view as code_improve_view
from modules.code_generate import view as code_generate_view
from modules.ui_design import view as ui_design_view


# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title=f"{APP_NAME} — Code Assistant",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": f"{APP_NAME} {APP_VERSION} — {APP_SUBTITLE}",
    },
)


# ── Load CSS ─────────────────────────────────────────────────────────────────
def _load_css() -> None:
    css_path = Path("assets/styles.css")
    if css_path.exists():
        css = css_path.read_text(encoding="utf-8")
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

_load_css()


# ── Session State ─────────────────────────────────────────────────────────────
if "active_module" not in st.session_state:
    st.session_state.active_module = "home"
if "selected_model" not in st.session_state:
    st.session_state.selected_model = DEFAULT_MODEL


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    # Logo
    st.markdown(
        f"""
        <div class="seaaa-logo">{APP_NAME}</div>
        <div class="seaaa-tagline">{APP_SUBTITLE}</div>
        <div class="seaaa-version">{APP_VERSION}</div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()

    # Navigation
    st.markdown("**Navigation**")

    nav_items = {
        "home":          ("🏠", "Home"),
        "error_fix":     ("🔴", "Fix Errors"),
        "code_improve":  ("🟡", "Improve Code"),
        "code_generate": ("🟢", "Generate Code"),
        "ui_design":     ("🔵", "UI Design Assistant"),
    }

    for key, (icon, label) in nav_items.items():
        is_active = st.session_state.active_module == key
        btn_label = f"{icon}  {label}"
        if is_active:
            st.button(btn_label, key=f"nav_{key}", use_container_width=True, type="primary")
        else:
            if st.button(btn_label, key=f"nav_{key}", use_container_width=True, type="secondary"):
                st.session_state.active_module = key
                st.rerun()

    st.divider()

    # Model Selection
    st.markdown("**AI Model**")
    model_keys   = list(AVAILABLE_MODELS.keys())
    model_labels = list(AVAILABLE_MODELS.values())
    selected_label = st.selectbox(
        "model",
        model_labels,
        index=model_keys.index(st.session_state.selected_model),
        label_visibility="collapsed",
        key="model_selector",
    )
    st.session_state.selected_model = model_keys[model_labels.index(selected_label)]

    st.divider()

    # ── GROQ API Key ─────────────────────────────────────────────────
    st.markdown("**GROQ API Key**")

    import os
    # Allow user to enter key at runtime if not set in environment
    if not os.environ.get("GROQ_API_KEY", ""):
        api_key_input = st.text_input(
            "Enter your GROQ API Key",
            type="password",
            placeholder="gsk_...",
            key="runtime_api_key",
            label_visibility="collapsed",
        )
        if api_key_input.strip():
            os.environ["GROQ_API_KEY"] = api_key_input.strip()
            # Reload config so llm_handler picks up the new key
            import core.config as cfg
            cfg.GROQ_API_KEY = api_key_input.strip()
            st.markdown(
                "<p style='color:#16a34a; font-size:0.73rem; font-family:monospace; margin:0;'>"
                "● API Key Set</p>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                "<p style='color:#dc2626; font-size:0.73rem; font-family:monospace; margin:0;'>"
                "● Key not set — enter above</p>",
                unsafe_allow_html=True,
            )
        st.caption("Get a free key at [console.groq.com](https://console.groq.com)")
    else:
        st.markdown(
            "<p style='color:#16a34a; font-size:0.73rem; font-family:monospace; margin:0;'>"
            "● API Connected</p>",
            unsafe_allow_html=True,
        )


# ── Main Panel ────────────────────────────────────────────────────────────────
model  = st.session_state.selected_model
module = st.session_state.active_module

if module == "home":

    # ── Hero ────────────────────────────────────────────────────────
    st.markdown(
        """
        <div style="text-align:center; padding: 2.5rem 0 1.5rem 0;">
            <div style="
                font-family: 'JetBrains Mono', monospace;
                font-size: 3rem;
                font-weight: 700;
                letter-spacing: 0.2em;
                color: #111827;
            ">DevAI</div>
            <div style="
                font-family: 'DM Sans', sans-serif;
                font-size: 0.7rem;
                color: #9ca3af;
                letter-spacing: 0.14em;
                text-transform: uppercase;
                margin-top: 0.3rem;
            ">Developer AI Code Assistant</div>
            <div style="
                font-family: 'DM Sans', sans-serif;
                font-size: 0.95rem;
                color: #4b5563;
                margin-top: 1.2rem;
                line-height: 1.7;
            ">
                A professional AI code assistant powered by Groq &amp; LLaMA 3.3.<br>
                Fix bugs &nbsp;·&nbsp; Improve code &nbsp;·&nbsp; Generate solutions &nbsp;·&nbsp; Design UIs
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # ── Feature cards — 2 × 2 grid ─────────────────────────────────
    cards = [
        ("🔴", "Fix Errors",
         "Paste your broken code. AI auto-detects the language and fixes every error — no extra input needed.",
         "error_fix"),
        ("🟡", "Improve Code",
         "Paste any working code. AI refactors, optimises, and applies best practices instantly.",
         "code_improve"),
        ("🟢", "Generate Code",
         "Describe what you want to build. AI generates complete, runnable code from scratch.",
         "code_generate"),
        ("🔵", "UI Design Assistant",
         "Describe any UI — logo, page, form, dashboard. AI generates the full code immediately.",
         "ui_design"),
    ]

    row1 = st.columns(2)
    row2 = st.columns(2)
    cols = row1 + row2

    for col, (icon, title, desc, key) in zip(cols, cards):
        with col:
            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="feature-card-icon">{icon}</div>
                    <div class="feature-card-title">{title}</div>
                    <div class="feature-card-desc">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if st.button("Open →", key=f"home_{key}", use_container_width=True):
                st.session_state.active_module = key
                st.rerun()

    st.divider()

    # ── Footer ──────────────────────────────────────────────────────
    st.markdown(
        """
        <div style="text-align:center; margin-top: 0.5rem;">
            <span style="
                font-family: 'JetBrains Mono', monospace;
                font-size: 0.65rem;
                color: #9ca3af;
                letter-spacing: 0.08em;
                text-transform: uppercase;
            ">
                Groq API &nbsp;·&nbsp; LLaMA 3.3 70B &nbsp;·&nbsp; Mixtral 8x7B &nbsp;·&nbsp; Gemma 2 9B
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif module == "error_fix":
    error_fix_view.render(model)

elif module == "code_improve":
    code_improve_view.render(model)

elif module == "code_generate":
    code_generate_view.render(model)

elif module == "ui_design":
    ui_design_view.render(model)
