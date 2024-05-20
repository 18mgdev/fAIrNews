import nltk
from nltk.corpus import stopwords
import string
import re

nltk.download('stopwords')

def clean_text(s):
    s = s.lower()
    s = re.sub(f'[{re.escape(string.punctuation)}]', '', s)
    return s

def remove_stop_words(s):
    stop_words = set(stopwords.words('spanish'))
    words = s.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)