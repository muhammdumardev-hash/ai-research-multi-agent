from crewai import Task


def create_writing_task(agent):

    return Task(
        description=(
            "Create the final research report using the research "
            "findings, sources, fact-checking results, and analysis "
            "provided by the research team. Organize the report "
            "clearly and professionally. Do not invent information."
        ),
        expected_output=(
            "A professional research report with a clear title, "
            "introduction, main findings, analysis, conclusion, "
            "and relevant sources."
        ),
        agent=agent
    )