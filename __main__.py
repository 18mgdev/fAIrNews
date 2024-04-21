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


#****************EXTRAER TOPICS


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import corpora, models

# Preparación de datos
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalpha() and word not in stopwords.words('spanish')]
    return tokens

def extract_topics(news_list, num_topics=6):
    texts = [preprocess_text(news) for news in news_list]
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    lda_model = models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)
    topics = lda_model.print_topics(num_words=4)
    # Asegurarse de que solo se extraigan las palabras, omitiendo las probabilidades
    topics_list = [" ".join([word for word, _ in lda_model.show_topic(topicid, topn=7)]) for topicid, _ in topics]
    return lda_model, dictionary, corpus, topics_list


def assign_topic_to_news(news, lda_model, dictionary):
    processed_news = preprocess_text(news)
    bow_news = dictionary.doc2bow(processed_news)
    topics = lda_model.get_document_topics(bow_news)
    main_topic = max(topics, key=lambda x: x[1])  # Selecciona el tema con la mayor probabilidad
    return main_topic

# Lista de noticias
news_list = [e["title"] for e in all_items]

# Extracción de los temas y obtención del modelo, diccionario y lista de topics
lda_model, dictionary, corpus, topics_list = extract_topics(news_list)

# Asignación de temas a cada noticia
news_topics = [(news, assign_topic_to_news(news, lda_model, dictionary)) for news in news_list]

# Mostrar los topics extraídos
for idx, topic in enumerate(topics_list):
    print(f"Topic {idx + 1}: {topic}")




# Asignar los topics a las noticias

for i in range(len(all_items)):
    all_items[i]["topic"] = news_topics[i][1][0]
    all_items[i]["topic_score"] = news_topics[i][1][1]


resumenes=[]
for i in range(len(topics_list)):
    resumenes.append([])

for i in range(len(all_items)):
    resumenes[all_items[i]["topic"]].append(all_items[i])

#en resumenes hemos agrupado las noticias por topic


import spacy
import math
# Suponemos que se carga el modelo en español
nlp = spacy.load("es_core_news_sm")
def summarize_article(text, num_sentences=5):
    # Procesar el texto con el modelo NLP
    doc = nlp(text)
    
    # Identificar y priorizar oraciones basadas en entidades nombradas y otros criterios
    sentences = list(doc.sents)
    print("num fases ", len(sentences))
    ranked_sentences = sorted(sentences, key=lambda s: len(s.ents), reverse=True)
    
    
    num_sentences = min(num_sentences, math.ceil(len(ranked_sentences)/3)) #divide entre 3 y redondea hacia arriba
    print("num frases a devolver ", num_sentences)
    # Compilar el resumen basado en las oraciones mejor clasificadas
    summary = " ".join([str(sentence) for sentence in ranked_sentences[:num_sentences]])
    
    return summary



#queda hacer el resumen de cada noticia:
import random
def summarize_articles_by_topic(topic_index, articles):
    """
    Genera un resumen de todas las noticias asociadas a un topic específico.

    Args:
    - topic_index (int): El índice del topic.
    - articles (list): Lista de artículos (diccionarios) que incluyen contenido y metadatos.

    Returns:
    - str: Resumen consolidado de las noticias del topic dado.
    """
    # Filtrar artículos por el topic especificado
    topic_articles = [article for article in articles if article["topic"] == topic_index]

    title = random.choice(topic_articles)["title"]
    # Concatenar el contenido de todos los artículos filtrados
    full_text = " ".join(article["content"] for article in topic_articles)

    # Utilizar la función de resumen en el texto completo
    summary = summarize_article(full_text)
    
    return title, summary

topic_index = 0  # Ajustar según el topic de interés
title, summary = summarize_articles_by_topic(topic_index, all_items)
print("Resumen del Topic:",title, "\n", summary)
