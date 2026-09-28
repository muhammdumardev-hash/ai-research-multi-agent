import os

from crewai import LLM


def get_llm():
    groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        raise ValueError("GROQ_API_KEY is not configured.")

    return LLM(
        model="groq/openai/gpt-oss-120b",
        api_key=groq_api_key,
        reasoning_effort="low"
    )