
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
