import spacy
from transformers import BertTokenizer, EncoderDecoderModel

model_name = 'mrm8488/bert2bert_shared-spanish-finetuned-summarization'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = EncoderDecoderModel.from_pretrained(model_name)
nlp = spacy.load("es_core_news_sm")
max_tokens=1000
def summarize_with_bert2bert(text, ml=500):

    inputs = tokenizer(text, return_tensors="pt", max_length=ml, truncation=True, padding="max_length")
    input_ids = inputs.input_ids
    attention_mask = inputs.attention_mask

    outputs = model.generate(input_ids=input_ids, attention_mask=attention_mask, max_length=ml, min_length=int(ml*0.4), num_beams=4, early_stopping=True)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return summary

def split_text(text, max_chunk_size=512):
    sentences = text.split('. ')
    chunks = []
    chunk = ""

    for sentence in sentences:
        if len(tokenizer(chunk + sentence, return_tensors="pt")['input_ids'][0]) <= max_chunk_size:
            chunk += sentence + '. '
        else:
            chunks.append(chunk.strip())
            chunk = sentence + '. '

    chunks.append(chunk.strip())
    return chunks

def remove_dashes(text):
    # Separar las frases del texto
    sentences = text.split('. ')
    cleaned_sentences = []

    # Procesar cada frase
    for sentence in sentences:
        # Si la frase empieza con " -", quitarlo
        if sentence.startswith('- '):
            sentence = sentence[2:]
        cleaned_sentences.append(sentence)

    # Volver a juntar las frases
    cleaned_text = '. '.join(cleaned_sentences)

    # Si el texto original termina en un punto, asegurarse de que el resultado también lo haga
    if text.endswith('.'):
        cleaned_text += '.'

    return cleaned_text

def get_num_tokens(text):
  return len(tokenizer(text, return_tensors="pt")['input_ids'][0])


def generate_summary(text, max_tokens):
  while get_num_tokens(text)>max_tokens:
    print("tokens actuales:", get_num_tokens(text))
    ml=min(512,int(get_num_tokens(text)*0.7))
    print("ml->", ml)
    aux=""
    chunks = split_text(text, max_chunk_size=ml)
    for chunk in chunks:
      aux += summarize_with_bert2bert(chunk, ml=ml) + ". "
    text=aux
  return remove_dashes(text)



# Función para extraer las mejores frases de un texto
def extract_key_sentences(text, num_sentences=6):
    doc = nlp(text)
    sentences = list(doc.sents)
    ranked_sentences = sorted(sentences, key=lambda s: len(s.ents), reverse=True)
    num_sentences=int(len(ranked_sentences)*0.5)
    selected_sentences = " ".join([str(sentence) for sentence in ranked_sentences[:num_sentences]])
    return selected_sentences





def generate_summary_from_list(texts:list, max_tokens_to_generate=max_tokens):
  summs=""
  for e in texts:
    summs+=e+". "
  texto=extract_key_sentences(summs)


  finstr=generate_summary(texto, max_tokens_to_generate)
  #finstr=extract_key_sentences(summs)
  return remove_dashes(finstr)

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

"""
def summarize_headlines(titulares:list):
    inputs = tokenizer(titulares, return_tensors="pt", truncation=True, padding="max_length")
    input_ids = inputs.input_ids
    attention_mask = inputs.attention_mask

    outputs = model.generate(input_ids=input_ids, attention_mask=attention_mask, max_length=40, min_length=20, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return summary

"""
