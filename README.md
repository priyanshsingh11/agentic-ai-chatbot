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

## agentic-chatbot/

### backend.py
FastAPI application responsible for API routing, request validation, and communication between the frontend and the LangGraph agent.

### ai_agent.py
Defines the LangGraph agent, including state management, reasoning logic, tool invocation, and LLM interaction.

### frontend.py
Streamlit-based user interface that handles user input, displays chat history, and renders AI responses.

### .env
Stores environment variables such as API keys for LLM providers and external tools.  
**This file should not be committed to version control.**

### requirements.txt
Lists all Python dependencies required to run the project.

### README.md
Project documentation describing system architecture, design principles, and usage instructions.

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

This project serves as a reference implementation for building agentic AI systems using LangGraph. It highlights how to structure conversational AI applications that go beyond simple prompt–response flows by introducing state, tools, and controlled execution paths.
system_design:
  project_name: agentic-ai-chatbot
  architecture_type: client-server
  paradigm: agentic-ai-with-state

  clients:
    - name: streamlit_frontend
      role: user_interface
      responsibilities:
        - collect_user_input
        - display_chat_history
        - send_requests_to_backend
        - render_ai_responses
      communication:
        protocol: HTTP
        method: POST
        endpoint: /chat

  backend:
    name: fastapi_server
    role: api_gateway
    responsibilities:
      - validate_requests
      - manage_request_schema
      - route_requests_to_agent
      - return_ai_response
    framework: FastAPI
    port: 9999

  agent_layer:
    name: langgraph_agent
    role: decision_and_reasoning_engine
    responsibilities:
      - maintain_conversation_state
      - reason_over_messages
      - decide_tool_usage
      - invoke_language_model
    framework: LangGraph
    agent_type: ReAct
    state:
      type: explicit
      structure:
        messages:
          - role: user | assistant
            content: string

  llm_layer:
    provider: configurable
    supported_providers:
      - Gemini
      - OpenAI
      - Groq
    responsibilities:
      - generate_text_responses
      - follow_system_prompt
    invocation_mode: synchronous

  tools:
    - name: tavily_search
      type: web_search
      optional: true
      triggered_by: agent_reasoning
      purpose: retrieve_external_information

  configuration:
    environment_variables:
      - GEMINI_API_KEY
      - OPENAI_API_KEY
      - GROQ_API_KEY
      - TAVILY_API_KEY
    config_source: .env

  data_flow:
    - step: user_input
      from: streamlit_frontend
      to: fastapi_backend
    - step: request_validation
      from: fastapi_backend
      to: fastapi_backend
    - step: agent_execution
      from: fastapi_backend
      to: langgraph_agent
    - step: llm_tool_interaction
      from: langgraph_agent
      to: llm_and_tools
    - step: response_generation
      from: langgraph_agent
      to: fastapi_backend
    - step: response_rendering
      from: fastapi_backend
      to: streamlit_frontend

  non_functional_requirements:
    scalability: moderate
    extensibility: high
    security:
      - api_keys_in_env
      - no_keys_exposed_to_client
    maintainability: high

  deployment_model:
    frontend: local_or_cloud
    backend: local_or_cloud
    dependency_management: pip_virtualenv
s
