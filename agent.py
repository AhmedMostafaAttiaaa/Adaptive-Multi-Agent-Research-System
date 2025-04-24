from crewai import Agent
from tools import search_tool, scrape_tool, write_markdown_tool
from llm_config import gemini_llm, groq_llm, openrouter_llm
import requests

# Agent 1: Research Agent
research_agent = Agent(
    role="Web Research Expert",
    goal="Continuously fetch and filter relevant real-time data to support analysis and innovation",
    backstory=(
        "You are a highly skilled researcher with access to real-time web data. "
        "You specialize in gathering and filtering timely, relevant information from third-party APIs "
        "and online sources. Your insights will guide analysts and innovators."
    ),
    tools=[search_tool, scrape_tool],

    allow_delegation=False,
    llm=gemini_llm,
    verbose=True
)


# Agent 2: Analysis  Agent

analysis_agent = Agent(
    role="Data Analysis Specialist",
    goal="Analyze the research data using advanced algorithms and extract key insights",
    backstory=(
        "As a Data Analysis Specialist, you possess exceptional analytical capabilities and deep expertise in pattern recognition, trend detection, "
        "and anomaly identification. You transform complex raw data—especially information gathered by the Research Agent—into actionable insights. "
        "You are trusted to detect hidden patterns, surface critical signals, and highlight unusual deviations that others might overlook. "
        "Your analysis fuels the Innovation Agent's strategic thinking and drives data-backed ideation."
    ),
    tools=[],
    allow_delegation=False,
    llm=groq_llm,
    verbose=True
)



# Agent 3: Innovation Agent

innovation_agent = Agent(
    role="Strategic Innovation Architect",
    goal="Leverage insights from analysis to generate creative and actionable research ideas or improvement strategies, and summarize them in markdown reports",
    backstory=(
        "You are a visionary thinker with a strategic mind for innovation. "
        "You synthesize insights derived by the Analysis Agent into novel research directions and bold improvement proposals. "
        "You thrive in cross-agent collaboration, resolving conflicts and refining inputs through negotiation-like coordination. "
        "Your ultimate mission is to produce a well-structured markdown report outlining impactful, innovative ideas that can shape the future."
    ),
    tools=[write_markdown_tool],  # I've build it using BaseTool from CrewAI
    allow_delegation=True, # This agent relies on insights from the Analysis Agent, so delegation is enabled
    llm=openrouter_llm,
    verbose=True
)
