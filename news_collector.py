import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'news_sources')))


from news_sources import m_20minutos, m_abc, m_cope, m_elconfidencial, m_lasexta, m_eldiario
from news_sources import sm_elcorreo, sm_elmundo,sm_elpais,sm_elperiodico,sm_lavanguardia,sm_lavozdegalicia

def get_all_news():
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
    
    add_news(m_20minutos.get_news_list())
    add_news(m_abc.get_news_list())
    add_news(m_cope.get_news_list())
    add_news(m_elconfidencial.get_news_list())
    add_news(m_lasexta.get_news_list())
    add_news(m_eldiario.get_news_list())
    add_news(sm_elcorreo.get_news_list())
    add_news(sm_elmundo.get_news_list())
    add_news(sm_elpais.get_news_list())
    add_news(sm_elperiodico.get_news_list())
    add_news(sm_lavanguardia.get_news_list())
    add_news(sm_lavozdegalicia.get_news_list())
        
    return {"num_medios":count_medio, "items":all_items}




#pruebas
import json
with open('news.json', 'w') as f:
    json.dump(get_all_news(), f)