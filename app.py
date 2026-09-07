import streamlit as st
from utils.skill_extractor import extract_skills
from utils.category_mapping import get_category

st.set_page_config(
    page_title="Skill Extraction",
    page_icon="💼",
    layout="centered"
)

# Login Page
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password")

# Skill Extraction Page
else:

    st.title("💼 Automatic Skill Extraction")
    st.write("Paste a job description to detect required skills and categories.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    job_description = st.text_area(
        "📝 Paste Job Description",
        placeholder="Looking for Data Analyst with SQL, Python, Power BI and Excel experience.",
        height=180
    )

    if st.button("🔍 Extract Skills"):

        if job_description.strip():

            detected_skills = extract_skills(job_description)

            st.subheader("🎯 Detected Skills")

            if detected_skills:
                st.success(", ".join(detected_skills))

                st.subheader("📂 Categories")

                for skill in detected_skills:
                    category = get_category(skill)
                    st.write(f"**{category}** → {skill}")

            else:
                st.warning("No skills detected.")

        else:
            st.warning("Please paste a job description first.")