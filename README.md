# Agentic AI Chatbot

An agent-based conversational AI application built using LangGraph, FastAPI, and Streamlit.  
This project demonstrates a clean and modular approach to designing a stateful AI system with a backend API and a lightweight frontend interface.

---

<hr/>

<h2>File Structure</h2>

<pre>
agentic-chatbot/
│
├── backend.py
├── ai_agent.py
├── frontend.py
├── .env
├── requirements.txt
└── README.md
</pre>

<hr/>


---

## Component Description

### backend.py
- Defines request and response schemas using Pydantic
- Exposes a `/chat` endpoint for frontend communication
- Performs basic validation before invoking the agent
- Acts as the orchestration layer between UI and AI logic

---

### ai_agent.py
- Initializes the selected language model provider
- Configures tools such as web search when enabled
- Builds a LangGraph ReAct agent
- Manages agent state and message flow
- Returns the final AI-generated response

---

### frontend.py
- Implements a chat-style interface using Streamlit
- Sends structured requests to the backend API
- Maintains local chat history for display purposes
- Provides configuration controls (model, system prompt, tools)

---

## Agent Architecture

- Built using LangGraph’s prebuilt ReAct agent
- Operates on explicit state (`messages`)
- Supports tool usage through conditional reasoning
- Ensures predictable execution via graph-based control flow

---

## Environment Configuration

All sensitive credentials are managed using environment variables:


The `.env` file should not be committed to version control.

---

## Design Principles

- Separation of concerns between UI, API, and agent logic
- Provider-safe and extensible model selection
- Minimal coupling between components
- Production-oriented project layout

---

## Summary  
The system follows a layered client–server architecture where the Streamlit frontend captures user input and forwards it to a FastAPI backend. The backend acts as an orchestration layer, invoking a LangGraph-based agent that manages stateful reasoning and optional tool usage. The agent interacts with the selected language model to generate responses, which are then returned back through the backend and rendered to the user in the frontend.

