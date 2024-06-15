import text_cleaner as f
import news_sources.rss2json as r2j

RSS_URL="https://www.elperiodico.com/es/rss/rss_portada.xml"
NAME="ElPeriodico"

def get_news_list():
    """
    Get news from elperiodico and return it as a JSON OBJECT list
    """
    items = r2j.get_JSON(RSS_URL)
    for e in items:
        e["medio"]=NAME
        e["title"]=f.rss_clean_html(e["title"])
        e["content"]=f.rss_clean_html(str(e["content"]).replace("Seguir leyendo...",""))
    return items