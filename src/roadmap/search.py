import os
from dotenv import load_dotenv
from langchain.tools import Tool
from langchain.utilities import SerpAPIWrapper


load_dotenv()


search = SerpAPIWrapper(
    serpapi_api_key=os.getenv("SERP_API_KEY")
)

google_search_tool = Tool(
    name="Google Search",
    func=search.run,
    description="Use this tool to find educational resources from Google Search for a given weeks's topics"
)
