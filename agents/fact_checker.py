from crewai import Agent

from config.llm import get_llm
from tools.research_tools import research_search_tool


def create_fact_checker():

    fact_checker = Agent(
        role="Fact Checker",
        goal=(
            "Verify the accuracy of research findings, identify "
            "unsupported claims, and highlight conflicting or "
            "uncertain information."
        ),
        backstory=(
            "You are a careful fact checker. You examine research "
            "findings critically, compare claims with available "
            "evidence, and use reliable online sources when needed "
            "to verify important claims."
        ),
        llm=get_llm(),
        tools=[research_search_tool],
        verbose=True
    )

    return fact_checker