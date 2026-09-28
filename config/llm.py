import streamlit as st
from crewai import LLM

# Workaround for CrewAI cache_breakpoint bug with Groq/LiteLLM
import crewai.llms.cache as crewai_cache

crewai_cache.mark_cache_breakpoint = lambda msg: msg


def get_llm():

    groq_api_key = st.secrets["GROQ_API_KEY"]
    groq_model = st.secrets["GROQ_MODEL"]

    return LLM(
        model=f"groq/{groq_model}",
        api_key=groq_api_key,
        reasoning_effort="low",
        max_tokens=450
    )
