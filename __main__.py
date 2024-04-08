import m_20minutos, m_abc, m_cope, m_elconfidencial, sm_elpais, m_lasexta

all_items = []
for e in m_20minutos.get_news_list():
    all_items.append(e)
for e in m_abc.get_news_list():
    all_items.append(e)
for e in m_cope.get_news_list():
    all_items.append(e)
for e in m_elconfidencial.get_news_list():
    all_items.append(e)
for e in sm_elpais.get_news_list():
    all_items.append(e)
for e in m_lasexta.get_news_list():
    all_items.append(e)



#****************HACER RESUMENES DE LAS NOTICIAS

import functions as f


abctitle="'Oppenheimer' arrasa en unos premios que se olvidan de Scorsese y hacen de menos a 'Barbie'"
abccontent="""
 <p>El PP no suelta la presa sobre la esposa del presidente del Gobierno, Pedro Sánchez, por las reuniones que mantuvo con la matriz de Air Europa unos días antes de que la aerolínea fuera rescatada con dinero público en 2020. El líder popular, Alberto Núñez Feijóo, avisó este miércoles a Sánchez de que <b>el PP impulsará una "investigación específica" sobre los vínculos Begoña Gómez</b> con esa empresa y su supuesta intermediación para el rescate, una investigación que será "parlamentaria" pero que, amenazó Feijóo, puede terminar llegando a los tribunales si el presidente no ofrece explicaciones.</p><p>En una intervención con un tono algo más sosegado que en las últimas semanas, Feijóo aseguró que Sánchez que "se equivoca" si cree que ha "resuelto las dudas de lo que ha pasado en su Gobierno y en su partido", una referencia muy poco velada a la conocida como trama Koldo, que se habría beneficiado de mordidas en la compra de mascarillas durante la pandemia. Al líder del PP también<b> le genera dudas "lo que ha pasado" en la "casa" del presidente</b>, en referencia a la esposa de Sánchez, a quien no llamó por su nombre.</p><p>"Se equivoca si cree que ha dado carpetazo" a ese asunto, espetó Feijóo, que prometió que si el presidente "vuelve a negarse a dar explicaciones" impulsará "una investigación específica sobre los asuntos que le afectan a su entorno más inmediato".<b> "Parlamentaria seguro, y judicial también</b>, si es necesaria", espetó el líder del PP. En respuesta, Sánchez ironizó con la "paciencia" que, dijo, tiene que tener para responder semanalmente a las mismas preguntas, y exigió a Feijóo que "plante cara a la corrupción" en el PP y "exija la dimisión a la señora [Isabel Díaz] Ayuso como presidenta de la Comunidad de Madrid" por las informaciones sobre el fraude fiscal que habría cometido su pareja.</p>
"""
text=f.clean_html(abccontent)


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
    news_list.append(e["title"])
print(len(news_list))

# Extraer los temas
extract_topics(news_list)

for e in all_items:
    print(e["title"])
    print("[", e["link"], "]")
    print()