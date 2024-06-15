NEWS_SOURCES=[
    {"name":"20minutos", "rss_url":"https://www.20minutos.es/rss"},
    {"name":"ABC", "rss_url":"https://www.abc.es/rss/2.0/portada/"},
    {"name":"COPE", "rss_url":"https://www.cope.es/api/es/news/rss.xml"},
    {"name":"ElConfidencial", "rss_url":"https://rss.elconfidencial.com/espana/"},
    {"name":"LaSexta", "rss_url":"https://www.lasexta.com/rss/351410.xml"},
    {"name":"ElDiario", "rss_url":"https://www.eldiario.es/rss/"},
    {"name":"ElCorreo", "rss_url":"https://www.elcorreo.com/rss/2.0/portada/"},
    {"name":"ElMundo", "rss_url":"https://e00-elmundo.uecdn.es/elmundo/rss/portada.xml"},
    {"name":"ElPais", "rss_url":"https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada"},
    {"name":"ElPeriodico", "rss_url":"https://www.elperiodico.com/es/rss/rss_portada.xml"},
    {"name":"LaVanguardia", "rss_url":"https://www.lavanguardia.com/rss/home.xml"},
    {"name":"LaVozDeGalicia", "rss_url":"https://www.lavozdegalicia.es/index.xml"}
]


def get_all_news(limit:int):
    """
    Devuelve una lista de rss JSONs con todas las noticias de todos los medios de '/news_sources'
    """
    all_items = []
    count_medio=0
    countid = 0
    seen_titles = set()
    
    def add_news(source_news):
        nonlocal count_medio
        count_medio += 1
        nonlocal countid
        for e in source_news:
            if e["title"] not in seen_titles:
                countid += 1
                e["id"] = countid
                all_items.append(e)
                seen_titles.add(e["title"])
    
    for e in NEWS_SOURCES:
        add_news(get_news_list(e["rss_url"], e["name"], limit))

        
    return {"num_medios":count_medio, "items":all_items}


import text_cleaner as f
import rss2json as r2j

def get_news_list(rss_url:str,source_name:str, limit):
    """
    Get news from rss_url and return it as a JSON OBJECT list
    """
    items = r2j.get_JSON(rss_url, items_limit=limit)
    for e in items:
        e["medio"]=source_name
        e["title"]=f.rss_clean_html(e["title"])
        content=str(e["content"])
        content=content.replace("Leer</a>","</a>")
        content=content.replace("Seguir leyendo...","")
        content=content.replace("Seguir leyendo","")
        e["content"]=f.rss_clean_html(content)
    return items