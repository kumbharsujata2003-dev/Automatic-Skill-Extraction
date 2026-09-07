
def get_category(skill):
    categories = {
        "Python": "Programming",
        "SQL": "Database",
        "Power BI": "BI",
        "Excel": "Analytics"
    }

    return categories.get(skill, "Other")
