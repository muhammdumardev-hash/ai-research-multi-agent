from crewai import Agent

from config.llm import get_llm


def create_analyst():

    analyst = Agent(
        role="Research Analyst",
        goal=(
            "Analyze the verified research findings and identify "
            "important patterns, trends, relationships, comparisons, "
            "and meaningful insights."
        ),
        backstory=(
            "You are an experienced research analyst. You take "
            "verified research findings and turn them into meaningful "
            "insights. You focus on patterns, comparisons, trends, "
            "implications, and evidence-based conclusions."
        ),
        llm=get_llm(),
        verbose=True
    )

    return analyst