import streamlit as st
from google import genai
from google.genai import types
from crewai.tools import BaseTool


class ResearchSearchTool(BaseTool):
    name: str = "Web Research Tool"

    description: str = (
        "Search the web for concise factual research findings and "
        "relevant sources."
    )

    def _run(self, query: str) -> str:

        client = genai.Client(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        grounding_tool = types.Tool(
            google_search=types.GoogleSearch()
        )

        config = types.GenerateContentConfig(
            tools=[grounding_tool]
        )

        response = client.models.generate_content(
            model=st.secrets["GEMINI_MODEL"],
            contents=(
                "Research this topic using Google Search. Return only "
                "the most important factual findings and up to 5 "
                "relevant sources. Keep the response concise. "
                "Do not write a long report.\n\n"
                f"Topic: {query}"
            ),
            config=config
        )

        return response.text or ""


research_search_tool = ResearchSearchTool()
