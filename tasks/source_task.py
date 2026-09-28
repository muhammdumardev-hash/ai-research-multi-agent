from crewai import Task


def create_source_task(agent):

    return Task(
        description=(
            "Use the direct web research findings provided below. "
            "Identify only the most relevant and credible sources already "
            "present in that material. Do not invent sources and do not "
            "perform another web search."
        ),
        expected_output=(
            "A concise source list containing no more than 5 sources, "
            "with one short sentence explaining what each source supports."
        ),
        agent=agent
    )
