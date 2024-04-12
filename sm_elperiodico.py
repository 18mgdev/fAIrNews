import functions as f
import api_rss2json as r2j

RSS_URL="https://www.elperiodico.com/es/rss/rss_portada.xml"
NAME="ElPeriodico"

def get_news_list():
    """
    Get news from elperiodico and return it as a JSON OBJECT list
    """
    items = r2j.get_JSON(RSS_URL)["items"]
    for e in items:
        e["medio"]=NAME
        e["title"]=f.clean_html(e["title"])
        e["content"]=f.clean_html(str(e["description"]).replace("Seguir leyendo...",""))
    return items