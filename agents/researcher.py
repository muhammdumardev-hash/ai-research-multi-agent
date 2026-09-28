from crewai import Agent

from config.llm import get_llm


def create_researcher():

    researcher = Agent(
        role="Research Specialist",
        goal=(
            "Research the given topic thoroughly and collect "
            "relevant, accurate, and useful information."
        ),
        backstory=(
            "You are an experienced research specialist. "
            "You investigate topics carefully, identify important "
            "information, and provide clear research findings "
            "that other members of the research team can use."
        ),
        llm=get_llm(),
        verbose=True
    )

    return researcher
