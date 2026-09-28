from crewai import Agent

from config.llm import get_llm


def create_fact_checker():

    fact_checker = Agent(
        role="Fact Checker",
        goal=(
            "Verify the accuracy of research findings, identify "
            "unsupported claims, and highlight conflicting or "
            "uncertain information."
        ),
        backstory=(
            "You are a careful fact checker. Examine the research "
            "findings and source information provided in your task "
            "context. Do not invent web sources or facts."
        ),
        llm=get_llm(),
        verbose=True
    )

    return fact_checker
