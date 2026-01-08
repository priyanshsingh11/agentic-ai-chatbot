# Agentic AI Chatbot

An agent-based conversational AI application built using LangGraph, FastAPI, and Streamlit.  
This project demonstrates a clean and modular approach to designing a stateful AI system with a backend API and a lightweight frontend interface.

---

## System Design Overview
Client (User)
|
v
Streamlit Frontend
|
v
FastAPI Backend
|
v
LangGraph Agent
|
v
LLM + Optional Tools (Search)
|
v
Response to Client


### Design Rationale
- The frontend is responsible only for user interaction
- The backend exposes a single, well-defined API
- Agent logic is fully encapsulated inside LangGraph
- LLM providers and tools are abstracted for easy replacement

---
# <hr/>

<h2>Tech Stack</h2>

<ul>
  <li><strong>Frontend:</strong> Streamlit</li>
  <li><strong>Backend:</strong> FastAPI</li>
  <li><strong>Agent Framework:</strong> LangGraph</li>
  <li><strong>LLM Providers:</strong> OpenAI, Gemini, Groq</li>
  <li><strong>Tools:</strong> Tavily Web Search (Optional)</li>
  <li><strong>Configuration:</strong> Python Dotenv (.env)</li>
  <li><strong>Language:</strong> Python</li>
</ul>

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
