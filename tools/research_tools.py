import streamlit as st
from groq import Groq
from crewai.tools import BaseTool


class ResearchSearchTool(BaseTool):
    name: str = "Web Research Tool"

    description: str = (
        "Search the web for information about the research topic. "
        "Use this tool to find facts, studies, reports, articles, "
        "and other relevant information."
    )

    def _run(self, query: str) -> str:

        client = Groq(
            api_key=st.secrets["GROQ_API_KEY"]
        )

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",

            messages=[
                {
                    "role": "user",
                    "content": (
                        "Search the web and research this topic. "
                        "Provide concise factual findings and "
                        "mention the sources.\n\n"
                        f"Topic: {query}"
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
            max_completion_tokens=1024,
        )

        return response.choices[0].message.content


research_search_tool = ResearchSearchTool()
