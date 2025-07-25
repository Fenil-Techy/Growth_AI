import streamlit as st 
from src.roadmap.generator import generator
from src.roadmap.agent import agent


st.title("📚 AI Roadmap Generator with Resources")

context = st.text_input("Learning Context (e.g. Python, AI for medicine)", "Python for Data Science")
time_period = st.text_input("Target Time Period (e.g. 8 weeks)", "8 weeks")
learnings = st.text_area("Prior Knowledge (topics to skip or shorten)", "Basic Python")

if st.button("Generate Roadmap"):
    with st.spinner("Generating roadmap..."):
        
        response = generator.invoke({"context":context, "time_period":time_period, "learnings":learnings})
        roadmap=response.content
        st.write(roadmap)
        # roadmap_lines=roadmap.strip().split("\n")
        # weeks=[]
        # current_week=None
        # current_topics=[]
        
        # for line in roadmap_lines:
        #     line=line.strip()
            
        #     if line.startswith("###"):
        #         if current_week is not None:
        #             weeks.append({
        #                 "week":current_week,
        #                 "topics":current_topics
        #             })
        #         current_week=line.replace("###","").strip()
        #         current_topics=[]
        #     elif line.startswith("-"):
        #         topic = line[1:].strip()  # Remove the '-' and spaces
        #         current_topics.append(topic)
        # if current_week is not None:
        #     weeks.append({
        #         "week": current_week,
        #         "topics": current_topics
        #     })
        
        # for w in weeks:
        #     st.write("📅", w["week"])
        #     for t in w["topics"]:
        #         st.write("  •", t)
        