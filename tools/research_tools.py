import streamlit as st
from groq import Groq
from crewai.tools import BaseTool


class ResearchSearchTool(BaseTool):
    name: str = "Web Research Tool"

    description: str = (
        "Search the web for concise factual research findings and "
        "relevant sources."
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
                        "Research this topic using web search. Return only "
                        "the most important factual findings and up to 5 "
                        "relevant sources. Keep the response concise. "
                        "Do not write a long report.\n\n"
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
            max_completion_tokens=512,
        )

        return response.choices[0].message.content or ""


research_search_tool = ResearchSearchTool()
