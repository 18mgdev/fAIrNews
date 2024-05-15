from bs4 import BeautifulSoup
import html


def rss_clean_html(html_content):

    html_content = html.unescape(html_content)
    # Parsear el contenido HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extraer el texto limpio sin etiquetas HTML
    text = soup.get_text()
    text = text.replace("»", "\"")
    text = text.replace("«", "\"")
    text = text.replace("“", "\"")
    text = text.replace("”", "\"")
    text = text.replace("‘", "\"")
    text = text.replace("’", "\"")
    text = text.replace(" | ", ". ")
    
    # Opcional: limpiar espacios extra y saltos de línea
    text = ' '.join(text.split())
    
    return text


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