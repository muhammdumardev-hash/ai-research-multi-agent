from crewai import Task


def create_fact_check_task(agent):

    return Task(
        description=(
            "Review the research summary and source list provided by the "
            "previous stages. Check claims for consistency with the "
            "provided evidence. Do not perform another web search and do "
            "not invent evidence."
        ),
        expected_output=(
            "A concise fact-check report listing verified claims, "
            "questionable claims, and important uncertainties. "
            "Use short bullet points."
        ),
        agent=agent
    )
