from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_ollama import ChatOllama
from src.roadmap.search import google_search_tool

llm = ChatOllama(model="llama3.1:8b")

agent = initialize_agent(
    tools=[google_search_tool],
    llm=llm,
    agent="structured-chat-zero-shot-react-description",
    verbose=True
)
