import text_cleaner as f
import news_sources.rss2json as r2j

RSS_URL="https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada"
NAME="ElPais"
#centro izquierda SIN CONTENIDO

def get_news_list():
    """
    Get news from elpais and return it as a JSON OBJECT list
    """
    items = r2j.get_JSON(RSS_URL)
    for e in items:
        e["medio"]=NAME
        e["title"]=f.rss_clean_html(e["title"])
        if "suscríbete" in e["content"] and "EL PAÍS" in e["content"]:
            e["content"]=f.rss_clean_html(str(e["description"]).replace("Seguir leyendo",""))
        else:
            e["content"]=f.rss_clean_html(str(e["content"]).replace("Seguir leyendo",""))
    return items