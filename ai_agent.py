from dotenv import load_dotenv
load_dotenv()

import os

from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage


# LLMs
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3
)

# Tool
search_tool = TavilySearchResults(max_results=4)

# System prompt
system_prompt = "You are an AI chatbot that acts smart, friendly, and helpful."

# Agent
agent = create_react_agent(
    model=groq_llm,
    tools=[search_tool],
    state_modifier=system_prompt
)

# Query
query = "Tell me about the crypto market in 2024."

state = {
    "messages": [
        ("user", query)
    ]
}

response = agent.invoke(state)
messages=response.get("messages")
ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
print(ai_messages[-1])
