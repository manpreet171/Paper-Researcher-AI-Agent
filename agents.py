from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Call the Gemini models
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Creating a researcher agent for finding academic papers
paper_researcher = Agent(
    role="Researcher",
    goal='Find the most recent and relevant academic papers on {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert in academic research, tasked with finding the latest and most impactful papers in your field."
        "Your goal is to identify and summarize key findings from recent research."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Creating a writer agent to write articles based on research
article_writer = Agent(
    role='Writer',
    goal='Write a comprehensive article based on the summaries of academic papers on {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "You are a skilled writer with a talent for distilling complex research into engaging and accessible articles."
        "Your goal is to create a narrative that highlights the key findings and implications of recent research."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
