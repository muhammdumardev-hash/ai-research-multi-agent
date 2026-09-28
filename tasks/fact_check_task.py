from crewai import Task


def create_fact_check_task(agent):

    return Task(
        description=(
            "Review the research findings and source information. "
            "Use the web research tool to independently verify "
            "important claims. Identify supported claims, "
            "unsupported claims, conflicting information, and "
            "information that requires further verification."
        ),
        expected_output=(
            "A fact-checking report that clearly identifies "
            "verified information, questionable claims, "
            "conflicting evidence, and areas of uncertainty."
        ),
        agent=agent
    )