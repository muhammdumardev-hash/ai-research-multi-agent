from crewai import Task


def create_analysis_task(agent):

    return Task(
        description=(
            "Analyze the research and fact-checking results provided by "
            "the previous stages. Focus on the most important patterns, "
            "comparisons, trends, implications, and evidence-based insights. "
            "Do not repeat the research."
        ),
        expected_output=(
            "A concise analysis with 5-7 key insights and short explanations."
        ),
        agent=agent
    )
