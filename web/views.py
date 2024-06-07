from django.http import  HttpRequest
from django.shortcuts import render

from mongodb_functions import get_ultima_portada, get_noticia
import re
import random

INDEX_NAME = "home.html"
READER_NAME="reader.html"

def frontpage(request: HttpRequest):
    """
    Renderiza la página principal
    """
    content = get_ultima_portada()
    phigh=[]
    pmedium=[]
    plow=[]
    for e in content["noticias"]:
        e["keyword"]=e["keyword"].upper()
        e["title"]=e["title"]
        e["brief_summary"]=truncar_texto(e["brief_summary"])+"..."
        if e["relevance"]>=6:
            phigh.append(e)
        elif e["relevance"]<=3:
            plow.append(e)
        else:
            pmedium.append(e)


    context = {
        "date": formatear_fecha(content["date"]),
        "num_articles": content["num_articles"],
        "num_keywords": content["num_keywords"],
        "num_generated_articles": content["num_generated_articles"],
        "num_sources": content["num_sources"],
        "high": phigh,
        "medium": pmedium,
        "low": plow
    }

    # Renderizar el template
    return render(request, INDEX_NAME, context)


def noticia_reader(request: HttpRequest, noticiaid: str):
    """
    Renderiza una noticia
    """
    content=get_noticia(noticiaid)
    #parrafos=[{texto,link_img,inline-left|right}]
    parrafos=[]
    lista_media=[]
    for link in content["media"]:
        lista_media.append({"link":link["link"],"type":link["type"]})
    for e in dividir_en_parrafos(content["summary"]):
        media=get_random_link_media(lista_media)
        parrafos.append({"texto":e,
                         "link_media":media["link"] if media!="" else "",
                         "type_media":media["type"] if media!="" else "",
                         "inline":random.choice(["inline-left","inline-right", "full-width"])})
    
    
    context = {
        "date": formatear_fecha(content["date"]),
        "title": content["title"],
        "parrafos": parrafos,
        "references":content["references"],
        "thumbnail":content["thumbnail"] if "thumbnail" in content else ""
    }

    # Renderizar el template
    return render(request, READER_NAME, context)


def dividir_en_parrafos(texto, num_frases=4):
    # Dividir el texto en frases utilizando expresiones regulares
    frases = re.split(r'(?<=[.!?]) +', texto)
    
    # Agrupar las frases en párrafos según num_frases
    parrafos = [' '.join(frases[i:i + num_frases]) for i in range(0, len(frases), num_frases)]
    
    return parrafos

def truncar_texto(texto, num_words=20):
    """
    Trunca el texto después de num_words palabras.
    
    Args:
        texto (str): El texto a truncar.
        num_words (int): El número máximo de palabras a incluir en el texto truncado.
    
    Returns:
        str: El texto truncado.
    """
    palabras = texto.split()
    if len(palabras) <= num_words:
        return texto
    else:
        return ' '.join(palabras[:num_words])

def get_random_link_media(lista):
    if not lista:
        return ""
    
    # Seleccionar un elemento aleatorio
    elemento_seleccionado = random.choice(lista)
    
    # Eliminar el elemento seleccionado de la lista
    lista.remove(elemento_seleccionado)
    
    return elemento_seleccionado

def formatear_fecha(fecha):
    # Diccionario de meses en español
    meses = {
        1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
        5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
        9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
    }
    
    dia = fecha.day
    mes = meses[fecha.month]
    año = fecha.year
    hora = fecha.strftime("%H:%M")
    
    return f"{dia} de {mes} {año}, {hora}"