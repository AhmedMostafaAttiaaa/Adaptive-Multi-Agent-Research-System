from crewai_tools import BaseTool

import requests

from crewai_tools import (
    SerperDevTool,
    ScrapeWebsiteTool,
    FileReadTool
)

# search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
read_file_tool = FileReadTool(file_path="./data_source.md")

# A search tool using serper API-key
search_tool = SerperDevTool(
    name="Serper Search",
    description="Search the internet for relevant data",
    search_url="https://google.serper.dev/search",
    api_key=os.environ["SERPER_API_KEY"]
)



class WriteMarkdownTool(BaseTool):
    name: str = "write_markdown_tool"
    description: str = (
        "Writes content to a Markdown file. "
        "Takes 'content' (markdown text) and 'filename' (optional, defaults to 'final_report.md')"
    )

    def _run(self, content: str, filename: str = "final_report.md") -> str:
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            return f"✅ Markdown report successfully written to '{filename}'"
        except Exception as e:
            return f"❌ Failed to write markdown file: {e}"

write_markdown_tool = WriteMarkdownTool()
