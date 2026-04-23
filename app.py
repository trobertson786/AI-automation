"""
General AI Business Assistant — Streamlit Web Demo
Adapt for any business by editing config.py only.
"""

import os
import anthropic
import streamlit as st
from dotenv import load_dotenv
from prompt_builder import build_system_prompt, build_opening_prompt, BUSINESS_CONFIG as C

load_dotenv()

SYSTEM_PROMPT = build_system_prompt()
OPENING_PROMPT = build_opening_prompt()


def get_client() -> anthropic.Anthropic:
    api_key = os.getenv("ANTHROPIC_API_KEY") or st.secrets.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        st.error("ANTHROPIC_API_KEY not set. Add it to your .env file or Streamlit secrets.")
        st.stop()
    return anthropic.Anthropic(api_key=api_key)


def get_ai_response(client: anthropic.Anthropic, messages: list) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        system=SYSTEM_PROMPT,
        messages=messages,
        max_tokens=400,
    )
    return response.content[0].text.strip()


def main():
    st.set_page_config(
        page_title=f"{C['name']} Assistant",
        page_icon=C["page_icon"],
        layout="centered",
    )

    st.markdown(
        f"""
        <div style='text-align: center; padding: 1rem 0 0.5rem 0;'>
            <h2 style='margin-bottom: 0.1rem;'>{C['page_icon']} {C['name']} Assistant</h2>
            <p style='color: grey; font-size: 0.9rem;'>
                {C['name']} · {C['tagline']}
            </p>
        </div>
        <hr style='margin-bottom: 1.5rem;'>
        """,
        unsafe_allow_html=True,
    )

    client = get_client()

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    f"Hi there! I'm the {C['name']} assistant — here to help you with "
                    f"{C['tagline'].lower()}. What can I help you with today?"
                ),
            }
        ]

    for msg in st.session_state.messages:
        avatar = C["page_icon"] if msg["role"] == "assistant" else "👤"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])

    if user_input := st.chat_input("Type your message..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user", avatar="👤"):
            st.markdown(user_input)

        with st.chat_message("assistant", avatar=C["page_icon"]):
            with st.spinner(""):
                reply = get_ai_response(client, st.session_state.messages)
            st.markdown(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})

    st.markdown(
        f"""
        <hr>
        <p style='text-align: center; color: grey; font-size: 0.75rem;'>
            {C['location']} · {C['phone']}
        </p>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
