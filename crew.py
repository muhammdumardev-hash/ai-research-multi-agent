from crewai import Crew, Process

from agents.researcher import create_researcher
from agents.source_researcher import create_source_researcher
from agents.fact_checker import create_fact_checker
from agents.analyst import create_analyst
from agents.writer import create_writer

from tasks.research_task import create_research_task
from tasks.source_task import create_source_task
from tasks.fact_check_task import create_fact_check_task
from tasks.analysis_task import create_analysis_task
from tasks.writing_task import create_writing_task


def create_research_crew(topic):

    # Create agents
    researcher = create_researcher()
    source_researcher = create_source_researcher()
    fact_checker = create_fact_checker()
    analyst = create_analyst()
    writer = create_writer()

    # Create tasks
    research_task = create_research_task(researcher)
    source_task = create_source_task(source_researcher)

    fact_check_task = create_fact_check_task(fact_checker)
    analysis_task = create_analysis_task(analyst)
    writing_task = create_writing_task(writer)

    # Add the research topic
    research_task.description += f"\n\nResearch topic: {topic}"
    source_task.description += f"\n\nResearch topic: {topic}"

    # Pass previous task results to the next tasks
    fact_check_task.context = [
        research_task,
        source_task
    ]

    analysis_task.context = [
        research_task,
        source_task,
        fact_check_task
    ]

    writing_task.context = [
        research_task,
        source_task,
        fact_check_task,
        analysis_task
    ]

    # Create Crew
    crew = Crew(
        agents=[
            researcher,
            source_researcher,
            fact_checker,
            analyst,
            writer
        ],
        tasks=[
            research_task,
            source_task,
            fact_check_task,
            analysis_task,
            writing_task
        ],
        process=Process.sequential,
        verbose=True
    )

    return crew