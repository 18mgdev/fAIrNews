from bs4 import BeautifulSoup
import html


def rss_clean_html(html_content):

    html_content = html.unescape(html_content)
    # Parsear el contenido HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extraer el texto limpio sin etiquetas HTML
    text = soup.get_text()
    text = text.replace("»", "\"")
    text = text.replace("«", "\"")
    text = text.replace("“", "\"")
    text = text.replace("”", "\"")
    text = text.replace("‘", "\"")
    text = text.replace("’", "\"")
    text = text.replace(" | ", ". ")
    
    # Opcional: limpiar espacios extra y saltos de línea
    text = ' '.join(text.split())
    
    return text


