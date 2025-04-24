from crewai import Task
import requests

def get_research_task(topic: str, agent) -> Task:
    """
    Create a research task for the given topic and agent,
    producing only a concise summary without any URLs or links.
    """
    return Task(
        description=(
            f"Conduct in-depth research about the given topic: '{topic}'.\n"
            "Your responsibilities include:\n"
            "1. Searching for recent and credible sources\n"
            "2. Extracting key facts, trends, and expert opinions\n"
            "3. Noting any conflicting viewpoints or statistics\n"
            "4. Summarizing findings in a clear and concise format\n"
            "⚠️ Please omit all URLs, links, and citations—provide only the narrative summary."
        ),
        expected_output=(
            "A clear, concise summary that includes:\n"
            "- Key facts and statistics\n"
            "- Emerging trends and technologies\n"
            "- Expert analysis and predictions"
        ),
        agent=research_agent,
        async_execution=False
    )


def get_analysis_task(research_data: str, agent) -> Task:
    """
    Create an analysis task for processing research data to extract meaningful insights.
    """
    return Task(
        description=(
            f"You have received the following research summary:\n\n'{research_data}'\n\n"
            "Your job is to analyze this data using advanced reasoning and techniques.\n"
            "Please:\n"
            "1. Detect important trends and behavioral patterns\n"
            "2. Highlight any unusual findings or gaps\n"
            "3. Extract useful insights that can support innovation\n"
            "4. Summarize your analysis in a clear and structured format"
        ),
        expected_output=(
            "Your output should be a concise analysis report including:\n"
            "- Key trends and patterns\n"
            "- Any anomalies or surprising findings\n"
            "- Actionable insights for decision making"
        ),
        agent=analysis_agent,
        async_execution=False
    )



def get_innovation_task(analysis_data: str, agent) -> Task:
    """
    Create an innovation task that transforms analysis insights into creative and actionable strategies.
    """
    return Task(
        description=(
            f"You've received the following analysis report:\n'{analysis_data}'\n\n"
            "Your responsibilities include:\n"
            "1. Synthesizing the provided analysis insights\n"
            "2. Brainstorming creative research ideas or improvement strategies\n"
            "3. Resolving any inconsistencies or conflicts in data\n"
            "4. Structuring a detailed **Markdown report** containing your innovative recommendations"
        ),
        expected_output=(
            "A clear, well-structured Markdown report that includes:\n"
            "- Summary of analysis insights\n"
            "- Novel research directions or strategies\n"
            "- Justifications for each proposal\n"
            "- Markdown formatting with proper structure and clarity"
        ),
        agent=innovation_agent,
        async_execution=False
    )
