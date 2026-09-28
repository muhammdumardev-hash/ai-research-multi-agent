from crewai import Task


def create_analysis_task(agent):

    return Task(
        description=(
            "Analyze the verified research findings and fact-checking "
            "results. Identify important patterns, trends, "
            "relationships, comparisons, implications, and "
            "meaningful insights. Base the analysis only on the "
            "information provided by the previous research stages."
        ),
        expected_output=(
            "A structured analysis containing key patterns, trends, "
            "comparisons, implications, and evidence-based insights."
        ),
        agent=agent
    )