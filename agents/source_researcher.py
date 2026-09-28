from crewai import Agent

from config.llm import get_llm


def create_source_researcher():

    source_researcher = Agent(
        role="Source Research Specialist",
        goal=(
            "Find relevant and reliable sources related to the "
            "research topic and identify information that can "
            "support the research findings."
        ),
        backstory=(
            "You are a source research specialist. Use the "
            "research findings available in your task context to "
            "identify and organize the most relevant sources. "
            "Do not invent sources."
        ),
        llm=get_llm(),
        verbose=True
    )

    return source_researcher
