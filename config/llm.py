import streamlit as st
from crewai import LLM


def get_llm():

    gemini_api_key = st.secrets["GEMINI_API_KEY"]
    gemini_model = st.secrets["GEMINI_MODEL"]

    return LLM(
        model=f"gemini/{gemini_model}",
        api_key=gemini_api_key,
        max_tokens=450
    )
