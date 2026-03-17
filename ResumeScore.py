import os
import streamlit as st
from langchain_openai import ChatOpenAI

st.title("AI Resume Analyzer")

#openai_api_key = st.text_input("Enter OpenAI API Key", type="password")
openai_api_key = os.getenv("OPENAI_API_KEY")
resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
job_desc = st.text_area("Paste Job Description")

if resume_file and job_desc and openai_api_key:
    # Extract text from resume (similar to PyPDFLoader)
    from langchain_community.document_loaders import PyPDFLoader
    import tempfile

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(resume_file.read())
        file_path = tmp_file.name

    loader = PyPDFLoader(file_path)
    resume_text = " ".join([doc.page_content for doc in loader.load()])

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=openai_api_key)

    prompt = f"""
    You are an AI Resume Analyzer.
    Compare the following resume with the job description.
    Provide:
    - Match score (0-100%)
    - Match skills/keywords
    - Missing skills/keywords
    - Suggestions for improvement

    Resume:
    {resume_text}

    Job Description:
    {job_desc}
    """

    response = llm.invoke(prompt)
    st.write(response.content)