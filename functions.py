from bs4 import BeautifulSoup


def html_to_text(html):
    """
    Convert HTML to text
    """
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()

def remove_seguir_leyendo(text):
    """
    Remove "Seguir leyendo" from text
    """
    return text.split("Seguir leyendo")[0]

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