import os
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.utilities.serpapi import SerpAPIWrapper

# Setup SerpAPI
os.environ["SERPAPI_API_KEY"] = "your_serpapi_key_here"
search = SerpAPIWrapper()

# Initialize LLM
llm = ChatOllama(model="llama3.1:8b")

# Prompt Template
TEMPLATE = """
You are an expert educational roadmap generator.

🎯 Your goal is to design a complete **week-wise roadmap** for learning `{context}` from scratch to an advanced level.

📅 Duration: {time_period}  
🎓 Learner’s Prior Knowledge: {learnings}  

---

🧠 **Instructions:**
- Build a practical, beginner-friendly roadmap.
- Skip or shorten any topics already known (see Prior Knowledge).
- Focus on what to learn each week – keep it clear and structured.
- Ensure smooth progression from basics to advanced.
- Do not assume prior deep knowledge unless specified.

✅ **Output Requirements:**
- Use structured Markdown format.
- Divide the roadmap into weeks (e.g., “Week 1”, “Week 2”, etc.).
- For each week:
  - Add a title for the focus of the week (e.g., “Python Basics”, “Web Scraping”).
  - Bullet-point the exact topics/concepts and subtopic/sub-concept to learn that week.
- Be concise, detailed
- Avoid unnecessary filler content and resources for now.

---

✍️ **Example Format:**

Week 1: Title
- Topic 1 :
  - Sub-topics 1


Begin the roadmap below:
"""

prompt = ChatPromptTemplate.from_messages([
    HumanMessagePromptTemplate.from_template(TEMPLATE)
])

generator=prompt | llm