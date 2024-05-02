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

print(len(all_items))



from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import re
import string

def clean_text(s):
    s = s.lower()
    s = re.sub(f'[{re.escape(string.punctuation)}]', '', s)
    return s
#.append("«").append("»")
def remove_stop_words(s):
    stop_words = set(stopwords.words('spanish'))
    words = s.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)

#lemmatizer = WordNetLemmatizer()  # Esto debería configurarse para funcionar con español, aquí solo es un placeholder

# Supongamos que all_items es tu lista de noticias
all_keywords = []
max_components = 10  # Número máximo de componentes SVD

for noticia in all_items:
    content = noticia["content"] if "content" in noticia else noticia["title"]
    content = remove_stop_words(content)
    content = clean_text(content)
    sentences = sent_tokenize(content)
    if content == "":
        noticia["keywords"] = []
        continue
    tfv = TfidfVectorizer(tokenizer=word_tokenize)
    corpus_transformed = tfv.fit_transform(sentences)
    num_features = corpus_transformed.shape[1]
    num_components = min(max_components, num_features - 1)  # Asegurar que num_components sea menos que num_features

    if num_components > 0:  # Solo proceder si hay suficientes características para SVD
        svd = TruncatedSVD(n_components=num_components)
        corpus_svd = svd.fit_transform(corpus_transformed)
        feature_scores = dict(zip(tfv.get_feature_names_out(), svd.components_[0]))
        topic_output = sorted(feature_scores, key=feature_scores.get, reverse=True)[:5]
        noticia["keywords"] = topic_output

        # Actualizar all_keywords
        for keyword in topic_output:
            found = next((item for item in all_keywords if item[0] == keyword), None)
            if found:
                found[1] += 1
            else:
                all_keywords.append([keyword, 1])
# Ordenar y mostrar palabras clave más frecuentes
all_keywords = sorted(all_keywords, key=lambda x: x[1], reverse=True)
for keyword in all_keywords:
    print(keyword)


titulares = []
contenido = ""
for noticia in all_items:
    if all_keywords[6][0] in noticia["keywords"]:
        
        print(noticia["title"]+"("+noticia["medio"]+")\n\n")
        print(noticia["content"]+"\n\n\n\n")
        titulares.append(noticia["title"])
        contenido+=noticia["content"]+"\n"
for e in titulares:
    print(e)

text=""
for e in titulares:
    text+=e+". "

# import torch
# from transformers import BertTokenizerFast, EncoderDecoderModel
# device = 'cuda' if torch.cuda.is_available() else 'cpu'
# ckpt = 'mrm8488/bert2bert_shared-spanish-finetuned-summarization'
# tokenizer = BertTokenizerFast.from_pretrained(ckpt)
# model = EncoderDecoderModel.from_pretrained(ckpt).to(device)

# def generate_summary(text):

#    inputs = tokenizer([text], padding="max_length", truncation=True, max_length=512, return_tensors="pt")
#    input_ids = inputs.input_ids.to(device)
#    attention_mask = inputs.attention_mask.to(device)
#    output = model.generate(input_ids, attention_mask=attention_mask)
#    return tokenizer.decode(output[0], skip_special_tokens=True)


# print("resumen 1")
# print(generate_summary(text))

from transformers import pipeline

# Inicializa las pipelines de resumen y traducción
summarizer = pipeline("summarization", model="google-t5/t5-base")
es_en_translator = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en")
en_es_translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es")

# Traduce el texto del español al inglés
translated_text = es_en_translator(text)[0]['translation_text']

# Genera el resumen en inglés
summary_in_english = summarizer(translated_text, max_length=30, min_length=10, do_sample=False)[0]['summary_text']

# Traduce el resumen de vuelta al español
summary_in_spanish = en_es_translator(summary_in_english)[0]['translation_text']

print("Resumen(TITULO):")
print(summary_in_spanish)



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



print("Resumen(NOTICIA):")
print(summarize_article(contenido, 5))




