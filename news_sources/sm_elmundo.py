import text_cleaner as f
import api_rss2json as r2j

RSS_URL="https://e00-elmundo.uecdn.es/elmundo/rss/portada.xml"
NAME="ElMundo"

def get_news_list():
    """
    Get news from elmundo and return it as a JSON OBJECT list
    """
    items = r2j.get_JSON(RSS_URL)["items"]
    for e in items:
        e["medio"]=NAME
        e["title"]=f.rss_clean_html(e["title"])
        e["content"]=f.rss_clean_html(str(e["description"]).replace("Leer</a>","</a>"))+"."
    return items