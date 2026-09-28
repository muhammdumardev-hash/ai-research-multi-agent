from crewai import Task


def create_source_task(agent):

    return Task(
        description=(
            "Find reliable and relevant sources for the research topic. "
            "Use the web research tool to identify useful articles, "
            "reports, studies, websites, and other credible sources. "
            "Explain what information each source supports."
        ),
        expected_output=(
            "A list of relevant sources with a short explanation "
            "of the information or claims supported by each source."
        ),
        agent=agent
    )