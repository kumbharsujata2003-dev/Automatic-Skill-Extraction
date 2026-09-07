
def extract_skills(text):
    skills = ["Python", "SQL", "Power BI", "Excel"]

    detected_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            detected_skills.append(skill)

    return detected_skills
