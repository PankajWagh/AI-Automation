import streamlit as st
import os
from langchain_openai import ChatOpenAI

st.title("AI Meeting Notes Generator")

meeting_text = st.text_area("Paste Meeting Transcript")

if meeting_text and openai_api_key:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=openai_api_key)

    prompt = f"""
    You are an AI Meeting Notes Generator.
    Summarize the following transcript into:
    - Meeting Summary
    - Key Decisions
    - Action Items (with assignees if mentioned)
    - Reminders
    - Risks 
    - Pending Approvals
    Transcript:
    {meeting_text}
    """

    response = llm.invoke(prompt)
    st.write(response.content)