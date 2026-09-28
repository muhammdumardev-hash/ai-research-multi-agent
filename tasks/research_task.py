from crewai import Task


def create_research_task(agent):

    return Task(
        description=(
            "Research the given topic thoroughly. "
            "Use the web research tool to find relevant and "
            "up-to-date information. Identify important facts, "
            "key concepts, statistics, and findings related to "
            "the topic."
        ),
        expected_output=(
            "A detailed research summary containing important "
            "facts, findings, and relevant information about the topic."
        ),
        agent=agent
    )