from crewai import Crew, Process
from tasks import research_papers_task, write_article_task
from agents import paper_researcher, article_writer

# Forming the research and writing crew
crew = Crew(
    agents=[paper_researcher, article_writer],
    tasks=[research_papers_task, write_article_task],
    process=Process.sequential,
)

# Function to run the crew and return the result
def run_crew(topic):
    result = crew.kickoff(inputs={'topic': topic})
    return result
