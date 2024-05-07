import m_20minutos, m_abc, m_cope, m_elconfidencial, m_lasexta
import sm_elcorreo, sm_elmundo,sm_elpais,sm_elperiodico,sm_lavanguardia,sm_lavozdegalicia
all_items = []
for e in m_20minutos.get_news_list():
    all_items.append(e)
for e in m_abc.get_news_list():
    all_items.append(e)
for e in m_cope.get_news_list():
    all_items.append(e)
for e in m_elconfidencial.get_news_list():
    all_items.append(e)
for e in m_lasexta.get_news_list():
    all_items.append(e)
for e in sm_elcorreo.get_news_list():
    all_items.append(e)
for e in sm_elmundo.get_news_list():
    all_items.append(e)
for e in sm_elpais.get_news_list():
    all_items.append(e)
for e in sm_elperiodico.get_news_list():
    all_items.append(e)
for e in sm_lavanguardia.get_news_list():
    all_items.append(e)
for e in sm_lavozdegalicia.get_news_list():
    all_items.append(e)





from sklearn.feature_extraction.text import TfidfVectorizer
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

from collections import defaultdict # Utilizar defaultdict para manejar contadores automáticamente

def generate_top_keywords(all_items, num_topics=4):
    """
    Genera palabras clave en el campo ['keywords'] para cada noticia en all_items y devuelve un TOP de las palabras clave más frecuentes (dict)
    """
    all_texts = [remove_stop_words(clean_text(item["title"] + " " + item["content"])) for item in all_items]
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(all_texts)
    feature_names = tfidf_vectorizer.get_feature_names_out()
    
    all_keywords = defaultdict(int)
    for idx, item in enumerate(all_items):
        feature_index = tfidf_matrix[idx,:].nonzero()[1]
        tfidf_scores = zip(feature_index, [tfidf_matrix[idx, x] for x in feature_index])
        sorted_items = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)[:num_topics]
        keywords = [feature_names[i] for i, score in sorted_items]
        item['keywords'] = keywords
        for keyword in keywords:
            all_keywords[keyword] += 1

    sorted_keywords = sorted(all_keywords.items(), key=lambda x: x[1], reverse=True)
    return sorted_keywords





from transformers import pipeline
def summarize_headlines(titulares:list):

    text=""
    for e in titulares:
        text+=e+". "
    # pipeline resumen
    summarizer = pipeline("summarization", model="google-t5/t5-base")
    # pipeline traducciones
    es_en_translator = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")
    en_es_translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")

    # Traduce el texto del español al inglés
    translated_text = es_en_translator(text)[0]['translation_text']

    # Genera el resumen en inglés
    summary_in_english = summarizer(translated_text, max_length=30, min_length=10, do_sample=False)[0]['summary_text']

    # Traduce el resumen de vuelta al español
    summary_in_spanish = en_es_translator(summary_in_english)[0]['translation_text']
    return summary_in_spanish



import spacy
import math

def summarize_articles(contents:list, num_sentences=5, model_name="es_core_news_sm"):
    text=""
    for e in contents:
        text+=e+". "
    nlp = spacy.load(model_name)

    #procesa el texto
    doc = nlp(text)
    
    # Identificar y priorizar oraciones basadas en entidades nombradas y otros criterios
    sentences = list(doc.sents)
    ranked_sentences = sorted(sentences, key=lambda s: len(s.ents), reverse=True)
    
    
    num_sentences = max(num_sentences, math.ceil(len(ranked_sentences)/3)) #divide entre 3 y redondea hacia arriba
    #junta el top de mejores frases
    summary = " ".join([str(sentence) for sentence in ranked_sentences[:num_sentences]])
    
    return summary



def generate_summs_json(all_items:list, top_keywords:list, min_rank_keyword=3):
    """
    Genera lista de resumenes en formato JSON
    """
    final_summs = []
    for keyword, rank in top_keywords:
        if rank < min_rank_keyword:
            break
        titles = []
        contents = []
        referencias=[]
        imagenes=[]
        index=0
        while index<len(all_items) and len(titles) < rank:
            noticia = all_items[index]
            if keyword in noticia["keywords"]: #dentro se mete la noticia
                titles.append(noticia["title"])
                contents.append(noticia["content"])
                referencias.append({
                    "title": noticia["title"],
                    "link": noticia["link"],
                    "source": noticia["medio"],
                    "keywords": noticia["keywords"]
                })
                if "enclosure" in noticia and noticia["enclosure"]!={} and "link" in noticia["enclosure"]:
                    imagenes.append({
                        "link": noticia["enclosure"]["link"]
                    })
                elif "enclosure" in noticia and noticia["enclosure"]!={} and "thumbnail" in noticia["enclosure"]:
                    imagenes.append({
                        "link": noticia["enclosure"]["thumbnail"]
                    })
            index+=1

        #se monta el json y se añade a la lista final
        final_summs.append(
            {
                "keyword": keyword,
                "relevance": rank,
                "title": summarize_headlines(titles).split(".")[0] if len(summarize_headlines(titles).split("."))>0 else summarize_headlines(titles),
                "summary": summarize_articles(contents),
                "references": referencias,
                "media": imagenes
            }
            )
    return final_summs
    

import json
# with open("noticias.json", "r", encoding="utf-8") as f:
#     all_items=json.load(f)
print("num noticias: ",len(all_items))

top_keywords = generate_top_keywords(all_items, num_topics=4)




for e in top_keywords:
    print(e) if e[1]>1 else None

final_summs=generate_summs_json(all_items, top_keywords, min_rank_keyword=3)


with open("summs1.json", "w", encoding="utf-8") as f:
    json.dump(final_summs, f, indent=4, ensure_ascii=False)



