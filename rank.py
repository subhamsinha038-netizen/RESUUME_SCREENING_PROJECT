job_skills = {"Python", "SQL", "Machine Learning", "Data Analysis", "HTML", "CSS", "JavaScript", "Pandas", "Numpy", "Scikit-Learn", "PyTorch"}

def calculatescore(candidate_skills):
    return len(set(candidate_skills) &
               set(job_skills))