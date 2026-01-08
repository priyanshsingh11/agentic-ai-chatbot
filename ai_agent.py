from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage


def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    # -------------------------
    # LLM Selection
    # -------------------------
    if provider == "Gemini":
        llm = ChatGoogleGenerativeAI(
            model=llm_id,
            temperature=0.3
        )
    else:
        return "Invalid provider. Use 'Gemini'"

    # -------------------------
    # Tools
    # -------------------------
    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    # -------------------------
    # Agent (Prebuilt LangGraph)
    # -------------------------
    agent = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )

    # -------------------------
    # State (Memory)
    # -------------------------
    state = {
        "messages": query
    }

    # -------------------------
    # Invoke Agent
    # -------------------------
    response = agent.invoke(state)

    messages = response.get("messages")
    ai_messages = [
        message.content
        for message in messages
        if isinstance(message, AIMessage)
    ]

    return ai_messages[-1]
