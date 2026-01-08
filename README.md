# Agentic AI Chatbot

An agent-based conversational AI application built using LangGraph, FastAPI, and Streamlit.  
This project demonstrates a clean and modular approach to designing a stateful AI system with a backend API and a lightweight frontend interface.

---

<hr/>

<h2>System Design</h2>

<h3>Architecture Overview</h3>
<ul>
  <li><strong>Project Name:</strong> Agentic AI Chatbot</li>
  <li><strong>Architecture Type:</strong> Client–Server</li>
  <li><strong>Paradigm:</strong> Agentic AI with Explicit State</li>
</ul>

<hr/>

<h3>Client Layer</h3>
<ul>
  <li><strong>Client:</strong> Streamlit Frontend</li>
  <li><strong>Role:</strong> User Interface</li>
  <li><strong>Responsibilities:</strong>
    <ul>
      <li>Collect user input</li>
      <li>Display chat history</li>
      <li>Send requests to backend</li>
      <li>Render AI-generated responses</li>
    </ul>
  </li>
  <li><strong>Communication:</strong>
    <ul>
      <li>Protocol: HTTP</li>
      <li>Method: POST</li>
      <li>Endpoint: <code>/chat</code></li>
    </ul>
  </li>
</ul>

<hr/>

<h3>Backend Layer</h3>
<ul>
  <li><strong>Service:</strong> FastAPI Server</li>
  <li><strong>Role:</strong> API Gateway</li>
  <li><strong>Framework:</strong> FastAPI</li>
  <li><strong>Port:</strong> 9999</li>
  <li><strong>Responsibilities:</strong>
    <ul>
      <li>Validate incoming requests</li>
      <li>Manage request and response schemas</li>
      <li>Route requests to the LangGraph agent</li>
      <li>Return AI-generated responses</li>
    </ul>
  </li>
</ul>

<hr/>

<h3>Agent Layer</h3>
<ul>
  <li><strong>Agent:</strong> LangGraph Agent</li>
  <li><strong>Role:</strong> Decision and Reasoning Engine</li>
  <li><strong>Framework:</strong> LangGraph</li>
  <li><strong>Agent Type:</strong> ReAct</li>
  <li><strong>Responsibilities:</strong>
    <ul>
      <li>Maintain conversation state</li>
      <li>Reason over messages</li>
      <li>Decide when to use tools</li>
      <li>Invoke the language model</li>
    </ul>
  </li>
  <li><strong>State Management:</strong>
    <ul>
      <li>State Type: Explicit</li>
      <li>Structure:
        <pre>
messages:
  - role: user | assistant
    content: string
        </pre>
      </li>
    </ul>
  </li>
</ul>

<hr/>

<h3>LLM Layer</h3>
<ul>
  <li><strong>Provider:</strong> Configurable</li>
  <li><strong>Supported Providers:</strong>
    <ul>
      <li>OpenAI</li>
      <li>Gemini</li>
      <li>Groq</li>
    </ul>
  </li>
  <li><strong>Responsibilities:</strong>
    <ul>
      <li>Generate AI responses</li>
      <li>Follow system prompts</li>
    </ul>
  </li>
  <li><strong>Invocation Mode:</strong> Synchronous</li>
</ul>

<hr/>

<h3>Tools</h3>
<ul>
  <li><strong>Tool Name:</strong> Tavily Search</li>
  <li><strong>Type:</strong> Web Search</li>
  <li><strong>Optional:</strong> Yes</li>
  <li><strong>Triggered By:</strong> Agent Reasoning</li>
  <li><strong>Purpose:</strong> Retrieve external information</li>
</ul>

<hr/>

<h3>Configuration</h3>
<ul>
  <li><strong>Configuration Source:</strong> <code>.env</code></li>
  <li><strong>Environment Variables:</strong>
    <ul>
      <li>GEMINI_API_KEY</li>
      <li>OPENAI_API_KEY</li>
      <li>GROQ_API_KEY</li>
      <li>TAVILY_API_KEY</li>
    </ul>
  </li>
</ul>

<hr/>

<h3>Data Flow</h3>
<ol>
  <li>User input is sent from Streamlit Frontend to FastAPI Backend</li>
  <li>Backend validates the request</li>
  <li>Request is routed to the LangGraph Agent</li>
  <li>Agent interacts with LLM and optional tools</li>
  <li>Response is generated and returned to the backend</li>
  <li>Frontend renders the response to the user</li>
</ol>

<hr/>

<h3>Non-Functional Requirements</h3>
<ul>
  <li><strong>Scalability:</strong> Moderate</li>
  <li><strong>Extensibility:</strong> High</li>
  <li><strong>Maintainability:</strong> High</li>
  <li><strong>Security:</strong>
    <ul>
      <li>API keys stored in environment variables</li>
      <li>No sensitive data exposed to the client</li>
    </ul>
  </li>
</ul>

<hr/>

<h3>Deployment Model</h3>
<ul>
  <li><strong>Frontend:</strong> Local or Cloud</li>
  <li><strong>Backend:</strong> Local or Cloud</li>
  <li><strong>Dependency Management:</strong> Python Virtual Environment (pip)</li>
</ul>

<hr/>



## Design Rationale
- The frontend is responsible only for user interaction
- The backend exposes a single, well-defined API
- Agent logic is fully encapsulated inside LangGraph
- LLM providers and tools are abstracted for easy replacement

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
**Summary:**  
The system follows a layered client–server architecture where the Streamlit frontend captures user input and forwards it to a FastAPI backend. The backend acts as an orchestration layer, invoking a LangGraph-based agent that manages stateful reasoning and optional tool usage. The agent interacts with the selected language model to generate responses, which are then returned back through the backend and rendered to the user in the frontend.

