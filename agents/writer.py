from crewai import Agent

from config.llm import get_llm


def create_writer():

    writer = Agent(
        role="Research Report Writer",
        goal=(
            "Create a clear, well-structured, professional research "
            "report using the verified research findings and analysis."
        ),
        backstory=(
            "You are an experienced research writer. You transform "
            "verified research findings and analytical insights into "
            "a clear, organized, and easy-to-understand final report. "
            "You do not invent facts and only use information provided "
            "by the research team."
        ),
        llm=get_llm(),
        verbose=True
    )

    return writer