from crewai import Task


def create_writing_task(agent):

    return Task(
        description=(
            "Write the final research report using the provided analysis, "
            "fact-checking results, and source list. Be clear and professional. "
            "Do not repeat large blocks of earlier research and do not invent facts."
        ),
        expected_output=(
            "A concise professional report with a title, brief introduction, "
            "key findings, analysis, conclusion, and sources. Keep it focused "
            "and avoid unnecessary repetition."
        ),
        agent=agent
    )
