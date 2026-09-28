import os

from groq import Groq
from crewai.tools import BaseTool


class ResearchSearchTool(BaseTool):
    name: str = "Web Research Tool"

    description: str = (
        "Search the live web for current and relevant information "
        "about a research topic. Use this tool to find recent facts, "
        "articles, studies, reports, and online information."
    )

    def _run(self, query: str) -> str:

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            return "Error: GROQ_API_KEY is not configured."

        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "user",
                    "content": (
                        "Research the following topic using browser search. "
                        "Return important findings and mention the sources "
                        "used.\n\n"
                        f"Research topic: {query}"
                    ),
                }
            ],
            tools=[
                {
                    "type": "browser_search"
                }
            ],
            tool_choice="required",
            reasoning_effort="low",
            max_completion_tokens=3000,
        )

        return response.choices[0].message.content


research_search_tool = ResearchSearchTool()