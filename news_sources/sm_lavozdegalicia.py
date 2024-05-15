import text_cleaner as f
import api.api_rss2json as r2j

RSS_URL="https://www.lavozdegalicia.es/index.xml"
NAME="LaVozDeGalicia"

def get_news_list():
    """
    Get news from lavozdegalicia and return it as a JSON OBJECT list
    """
    items = r2j.get_JSON(RSS_URL)["items"]
    for e in items:
        e["medio"]=NAME
        e["title"]=f.rss_clean_html(e["title"])+"."
        e["content"]=f.rss_clean_html(str(e["content"]))+"."
    return items