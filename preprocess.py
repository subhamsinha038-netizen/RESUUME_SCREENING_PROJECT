import ssl
import re
import nltk
from nltk.corpus import stopwords

ssl._create_default_https_context = ssl._create_unverified_context

nltk.download('stopwords', quiet=False)
stop_words = set(stopwords.words('english'))

def clean_resume(text):
    text = str(text).lower()
    text = re.sub(r'http\S+','',text)
    text = re.sub(r'\S+@\S+','',text)
    text = re.sub(r'[^A-Za-z]','',text)
    text = re.sub(r'\s+','',text)
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)