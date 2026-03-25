skills_list = {"Python", "Java", "SQL", "Machine Learning", "Data Analysis", "HTML", "CSS", "JavaScript", "Pandas", "Numpy", "Scikit-Learn", "PyTorch"}

def extract_skills(text):
    skills_found = []
    for skill in skills_list:
            if skill.lower() in text.lower():
                  skills_found.append(skill)
    return skills_found        
