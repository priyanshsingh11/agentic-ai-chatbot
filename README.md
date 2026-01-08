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
# Project Structure
<h1>Project Structure</h1>

<h2>agentic-chatbot/</h2>

<h2>backend.py</h2>
<p>
FastAPI application responsible for API routing, request validation, and
orchestrating communication between the frontend and the LangGraph agent.
</p>

<h2>ai_agent.py</h2>
<p>
Defines the LangGraph agent, including state management, reasoning logic,
tool invocation, and interaction with the language model.
</p>

<h2>frontend.py</h2>
<p>
Streamlit-based user interface that collects user input, displays chat history,
and renders AI-generated responses.
</p>

<h2>.env</h2>
<p>
Stores environment variables such as API keys for LLM providers and external tools.
This file should not be committed to version control.
</p>

<h2>requirements.txt</h2>
<p>
Contains the list of Python dependencies required to run the project.
</p>

<h2>README.md</h2>
<p>
Project documentation describing the system architecture, design decisions,
and usage instructions.
</p>

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
