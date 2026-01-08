import streamlit as st
import requests

# -----------------------------
# Backend API URL
# -----------------------------
API_URL = "http://127.0.0.1:9999/chat"

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="LangGraph AI Agent",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 LangGraph AI Agent (Gemini)")
st.caption("Streamlit Frontend connected to FastAPI + LangGraph")

# -----------------------------
# Sidebar Controls
# -----------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    model_name = st.selectbox(
        "Select Gemini Model",
        ["gemini-1.5-flash", "gemini-1.5-pro"]
    )

    allow_search = st.checkbox("Enable Web Search (Tavily)", value=True)

    system_prompt = st.text_area(
        "System Prompt",
        value="You are a smart, friendly, and helpful AI assistant.",
        height=120
    )

# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Chat Messages
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# User Input
# -----------------------------
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message to UI
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # -------------------------
    # Prepare API Payload
    # -------------------------
    payload = {
        "model_name": model_name,
        "model_provider": "Gemini",
        "system_prompt": system_prompt,
        "messages": [user_input],
        "allow_search": allow_search
    }

    # -------------------------
    # Call Backend API
    # -------------------------
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(API_URL, json=payload, timeout=120)

                if response.status_code == 200:
                    ai_response = response.json()
                else:
                    ai_response = "Error: Unable to get response from server"

            except Exception as e:
                ai_response = f"Error: {str(e)}"

        st.markdown(ai_response)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })
