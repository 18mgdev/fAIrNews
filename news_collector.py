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
    count=0
    for e in m_20minutos.get_news_list():
        count+=1
        e["id"]=count
        all_items.append(e)
    for e in m_abc.get_news_list():
        count+=1
        e["id"]=count
        all_items.append(e)
    for e in m_cope.get_news_list():
        count+=1
        e["id"]=count
        all_items.append(e)
    for e in m_elconfidencial.get_news_list():
        count+=1
        e["id"]=count
        all_items.append(e)
    for e in m_lasexta.get_news_list():
        count+=1
        e["id"]=count
        all_items.append(e)
    for e in m_eldiario.get_news_list():
        count+=1
        e["id"]=count
        all_items.append(e)
    for e in sm_elcorreo.get_news_list():
        count+=1
        e["id"]=count
        all_items.append(e)
    for e in sm_elmundo.get_news_list():
        count+=1
        e["id"]=count
        all_items.append(e)
    for e in sm_elpais.get_news_list():
        count+=1
        e["id"]=count
        all_items.append(e)
    for e in sm_elperiodico.get_news_list():
        count+=1
        e["id"]=count
        all_items.append(e)
    for e in sm_lavanguardia.get_news_list():
        count+=1
        e["id"]=count
        all_items.append(e)
    for e in sm_lavozdegalicia.get_news_list():
        count+=1
        e["id"]=count
        all_items.append(e)
        
    return all_items



#pruebas
import json
with open('news.json', 'w') as f:
    json.dump(get_all_news(), f)