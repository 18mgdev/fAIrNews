from newsapi import NewsApiClient, const

api = NewsApiClient(api_key='c1d834f6006a48fd8ee6886dbf7cc40a')

all_items = api.get_everything(language='es', q="decapita", sort_by="publishedAt")['articles']
#print(api.get_sources(language='es'))
print(len(all_items))
for e in all_items:
    print(e["publishedAt"],e["source"]["name"]+": "+e["title"])

import spacy
import math

# Suponemos que se carga el modelo en español
nlp = spacy.load("es_core_news_sm")

def summarize_article(text):
    # Procesar el texto con el modelo NLP
    doc = nlp(text)
    
    # Identificar y priorizar oraciones basadas en entidades nombradas y otros criterios
    sentences = list(doc.sents)
    ranked_sentences = sorted(sentences, key=lambda s: len(s.ents), reverse=True)
    
    num_sentences = min(num_sentences, len(ranked_sentences))
    num_sentences=math.ceil(len(ranked_sentences)/3) #divide entre 3 y redondea hacia arriba

    # Compilar el resumen basado en las oraciones mejor clasificadas
    summary = " ".join([str(sentence) for sentence in ranked_sentences[:num_sentences]])
    
    return summary

#print(summarize_article(text))

#****************EXTRAER TOPICS


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import corpora, models
import re

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # Limpiar y tokenizar el texto
    tokens = word_tokenize(text.lower())
    # Eliminar palabras comunes y caracteres no alfabéticos
    tokens = [word for word in tokens if word.isalpha() and word not in stopwords.words('spanish')]
    return tokens

def extract_topics(news_list, num_topics=5):
    # Preprocesar cada noticia
    texts = [preprocess_text(news) for news in news_list]
    
    # Crear un diccionario y corpus para LDA
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    
    # Aplicar LDA
    lda_model = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)
    
    # Imprimir los temas encontrados
    topics = lda_model.print_topics(num_words=4)
    for topic in topics:
        print(topic)

# Lista de noticias
news_list = []
for e in all_items:
    if str(e["content"]).__contains__("terrorista"):
        print("si")
    news_list.append(e["content"])
print(len(news_list))

# Extraer los temas
extract_topics(news_list)
