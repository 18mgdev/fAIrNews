from bs4 import BeautifulSoup
import re
import html


def clean_html(html_content):

    html_content = html.unescape(html_content)
    # Parsear el contenido HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extraer el texto limpio sin etiquetas HTML
    text = soup.get_text()
    
    # Opcional: limpiar espacios extra y saltos de línea
    text = ' '.join(text.split())
    
    return text


def clean_title_AMPs(text): #EN DESUSO, se usa la de arriba
    """
    Eliminar cadenas no deseables en el titulo. Ejemplo: El PSOE se dice &amp;quot;tajante&amp;quot; frente a Aragonès: &amp;quot;Ni hay ni habrá referéndum&amp;quot; 
    """
    text = text.replace("&amp;quot;", "\"")
    text = text.replace("&quot;", "\"")
    text = re.sub(r"&amp;.*?;", "", text)

    return text

# {
#     status: "ok",
#     feed: {
#         "url": "https://www.20minutos.es/rss",
#         "title": "20minutos.es - Últimas Noticias",
#         "link": "https://www.20minutos.es",
#         "author": "",
#         "description": "20minutos.es, las noticias de última hora",
#         "image": "https://www.20minutos.es/img/logo.png"
#     },
#     items:[{title, pubDate, link, guid, author, thumbnail, description, content, enclosure:{link,type}, categories:[] }]

# }