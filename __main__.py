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
    news_list.append(e["title"])


# Extraer los temas
extract_topics(news_list)
