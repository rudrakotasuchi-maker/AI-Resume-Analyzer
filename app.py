import streamlit as st
from PyPDF2 import PdfReader

skills = [
    "python",
    "java",
    "sql",
    "machine learning",
    "data science",
    "html",
    "css",
    "javascript",
    "react",
    "pandas"
]

st.title("AI Resume Analyzer + ATS Score Checker")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)
analyze = st.button("Analyze Resume")

if analyze and uploaded_file and job_description:
   


    pdf = PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf.pages:
        resume_text += page.extract_text()

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    matched_skills = []

    for skill in skills:
        if skill in resume_text and skill in job_description:
            matched_skills.append(skill)

    ats_score = (
        len(matched_skills)
        / len(skills)
    ) * 100

    st.subheader("Matched Skills")
    st.write(matched_skills)

    st.subheader("ATS Score")
    st.write(round(ats_score, 2), "%")

    missing_skills = []

    for skill in skills:
        if skill in job_description and skill not in resume_text:
            missing_skills.append(skill)

    st.subheader("Missing Skills")
    st.write(missing_skills)