import pandas as pd
from preprocess import clean_resume
from skill_extractor import extract_skills
from rank import calculatescore
df = pd.read_csv("gpt_dataset.csv")
#print(df.head())

if 'Resume' not in df.columns:
    print("Error : 'Resume' column not found in dataset")
    exit()

cleaned_resumes = df['Resume'].apply(clean_resume)

df['skills'] = cleaned_resumes.apply(extract_skills)        

df['scores'] = df['skills'].apply(calculatescore)

df['ranks'] = df['scores'].rank(ascending=False)

print(df[['Category', 'skills', 'scores', 'ranks']].head())
