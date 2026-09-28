from crewai import Task


def create_research_task(agent):

    return Task(
        description=(
            "Use the direct web research findings provided below. "
            "Extract only the most important facts, findings, statistics, "
            "and key points for the topic. Do not perform additional web "
            "searches and do not repeat the full source material."
        ),
        expected_output=(
            "A concise research summary with no more than 8 key findings. "
            "Keep each finding short and factual."
        ),
        agent=agent
    )
