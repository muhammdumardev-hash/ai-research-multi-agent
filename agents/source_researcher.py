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
            "You are a source research specialist who focuses on "
            "finding useful and credible sources. You carefully "
            "look for reports, articles, studies, and other "
            "relevant sources that can support a research project."
        ),
        llm=get_llm(),
        verbose=True
    )

    return source_researcher