from crewai import Task
from tools import tool
from agents import paper_researcher, article_writer

# Research task: Search for relevant papers published after 2022
research_papers_task = Task(
    description=(
        "Search for four relevant academic papers published after 2022 on the topic {topic}."
        "The papers should be the most recent and highly cited in the field."
        "Summarize the key findings and relevance of each paper."
    ),
    expected_output='A summary of four academic papers published after 2022 on {topic}.',
    tools=[tool],
    agent=paper_researcher,
)

# Writing task: Write an article based on the papers found
write_article_task = Task(
    description=(
        "Compose an insightful article based on the summaries of the four academic papers on {topic}."
        "Focus on synthesizing the information into a coherent and engaging narrative."
        "The article should highlight the key findings and their implications."
    ),
    expected_output='A comprehensive article on {topic} advancements formatted as markdown.',
    tools=[tool],
    agent=article_writer,
    async_execution=False,
    output_file='article-based-on-papers.md'  # Example of output customization
)
