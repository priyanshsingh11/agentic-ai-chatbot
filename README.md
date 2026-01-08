# Agentic AI Chatbot

An agent-based conversational AI application built using LangGraph, FastAPI, and Streamlit.  
This project demonstrates a clean and modular approach to designing a stateful AI system with a backend API and a lightweight frontend interface.

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

## Digram
```mermaid
flowchart LR

    %% Client Layer
    subgraph Client
        U[User]
        FE[Frontend<br/>Streamlit / React]
        U -->|actions| FE
    end

    %% Backend Layer
    subgraph Backend
        API[FastAPI<br/>REST API]
        AG[LangGraph Agent<br/>Stateful Controller]

        RS[risk_scoring.py]
        RG[report_generator.py]
        GA[graph_analysis.py]
        CM[case_manager.py]
        AS[ai_summarizer.py]

        API --> AG
        AG --> RS
        AG --> RG
        AG --> GA
        AG --> CM
        AG --> AS
    end

    %% Data Sources
    subgraph Data_Sources["Data Sources"]
        CSV[CSV Files<br/>generated-data]
        NEO[Neo4j<br/>(optional)]
        FS[Firestore<br/>(optional)]
    end

    %% External Services
    LLM[LLM Provider<br/>OpenAI / Groq]
    WS[Web Search Tool]

    %% Connections
    FE -->|JSON / CSV Upload| API
    API -->|Response| FE

    AG -->|Prompt| LLM
    LLM -->|Completion| AG

    AG -->|Query| WS
    WS -->|Results| AG

    RS -->|AlertScores.csv| CSV
    GA --> NEO
    CM --> FS
```
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

