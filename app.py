import streamlit as st
from PyPDF2 import PdfReader
import matplotlib.pyplot as plt

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

    for skill in matched_skills:
        st.markdown(
        f"""
        <span style="
        background-color:green;
        color:white;
        padding:6px;
        border-radius:10px;
        margin:4px;
        display:inline-block;">
        {skill}
        </span>
        """,
        unsafe_allow_html=True
       )

    st.subheader("ATS Score")

    st.progress(int(ats_score))

    st.metric(
    label="ATS Score",
    value=f"{round(ats_score,2)}%"
    )
    st.subheader("Skills Match Analysis")

    matched_count = len(matched_skills)

    missing_count = len(skills) - len(matched_skills)

    fig, ax = plt.subplots()

    ax.pie(
     [matched_count, missing_count],
      labels=["Matched", "Missing"],
      autopct="%1.1f%%"
    )

    st.pyplot(fig)

   
   missing_skills = []

   for skill in skills:
       if skill in job_description and skill not in resume_text:
        missing_skills.append(skill)

   st.subheader("Missing Skills")

   if missing_skills:
       for skill in missing_skills:
        st.write("❌", skill)
   else:
       st.success("No missing skills found")
