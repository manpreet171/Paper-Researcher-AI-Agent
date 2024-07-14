# Paper Researcher AI Agent

This project leverages CrewAI and Google Generative AI (Gemini) to create a collaborative AI platform for researching and writing articles based on academic papers.

## Overview

The project involves setting up AI agents to perform specific tasks using a large language model (LLM). The main components include:

- **Researcher Agent**: Finds relevant academic papers published after 2022.
- **Writer Agent**: Composes articles based on the research findings.
- **Tools**: Utilities or services used by agents to perform tasks.
- **LLM**: Large language model used by agents for generating responses.

## Project Structure

The project directory structure is as follows:

Paper-Researcher-AI-Agent/
├── agents.py
├── app.py
├── crew.py
├── tasks.py
├── tools.py
├── requirements.txt
└── .env



## Setup

### Prerequisites

- Python 3.10 or later (<= 3.13)
- Git

### Steps to Set Up the Project

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/manpreet171/Paper-Researcher-AI-Agent.git
    cd Paper-Researcher-AI-Agent
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    - Create a `.env` file in the project root directory and add your API keys:
      ```plaintext
      GOOGLE_API_KEY=your_google_api_key_here
      SERPER_API_KEY=your_serper_api_key_here
      ```

5. **Run the Streamlit App**:
    ```bash
    streamlit run app.py
    ```

## Detailed Explanation

### agents.py

Defines the agents with their roles, goals, and backstories. It initializes the Google Generative AI model and sets up the Researcher and Writer agents. These agents use the `SerperDevTool` for internet searching capabilities.

### tasks.py

Defines the tasks for the agents. The Researcher agent is tasked with finding academic papers published after 2022, while the Writer agent is responsible for composing an article based on the research findings.

### crew.py

Sets up the crew of agents and defines the process for executing tasks sequentially. It includes a function to run the crew and return the results.

### tools.py

Initializes the `SerperDevTool` for internet searching capabilities. This tool is used by the agents to find relevant information on the internet.

### app.py

Creates a Streamlit app to handle user interaction. Users can input a topic, start the agent conversation, and view the final article output.

## Libraries Used

- **CrewAI**: For creating and managing AI agents and their tasks.
- **langchain-google-genai**: For integrating Google Generative AI (Gemini).
- **Streamlit**: For building the web interface.
- **dotenv**: For managing environment variables.
- **crewai_tools**: Provides additional tools like `SerperDevTool` for internet searching.


## Contact

If you have any questions or suggestions, feel free to reach out at [https://www.linkedin.com/in/manpreet17/].