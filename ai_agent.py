from dotenv import load_dotenv
import os
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage, HumanMessage


def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider != "Gemini":
        return "Invalid provider"

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing")

    llm = ChatGoogleGenerativeAI(
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        api_key=api_key
    )

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )

    state = {
        "messages": [HumanMessage(content=msg) for msg in query]
    }

    response = agent.invoke(state)

    ai_messages = [
        msg.content
        for msg in response.get("messages", [])
        if isinstance(msg, AIMessage)
    ]

    return ai_messages[-1] if ai_messages else "No response"
