import re
from src.roadmap.agent import agent

def extract_topics(roadmap_markdown: str):
    lines = roadmap_markdown.split('\n')
    topics = []

    for line in lines:
        if re.search(r'(week|milestone)', line, re.IGNORECASE):
            current_topic = line.strip()
        elif line.strip().startswith("-") or line.strip().startswith("*"):
            topics.append(line.strip("-* ").strip())

    return topics

def find_resources_for_topics(topics: list):
    topic_resources = {}

    for topic in topics:
        try:
            query = f"Find 2-3 high-quality free resources to learn: Prefer  articles, videos, or courses with direct links."
            result = agent.run(query)
            topic_resources[topic] = result
        except Exception as e:
            topic_resources[topic] = f"Error fetching resources: {str(e)}"

    return topic_resources
