from crewai import Crew
from task import get_research_task, get_analysis_task, get_innovation_task
from agent import research_agent, analysis_agent , innovation_agent
# Define the dynamic function to run the workflow
def run_ai_workflow(inputs: dict):
    # 1) Research the AI-related topic (this could be any topic you want)
    research_task = get_research_task(
        topic=inputs["topic"],
        agent=research_agent
    )

    # 2) Analyze the research output
    analysis_task = get_analysis_task(
        research_data=research_task,  
        agent=analysis_agent
    )

    # 3) Innovate on the analysis
    innovation_task = get_innovation_task(
        analysis_data=analysis_task,
        agent=innovation_agent
    )

    # 4) Create the Crew to tie everything together
    crew = Crew(
        agents=[research_agent, analysis_agent, innovation_agent],
        tasks=[research_task, analysis_task, innovation_task],
        verbose=True
    )

    # 5) Run the entire workflow and return the final output
    return crew.kickoff()

