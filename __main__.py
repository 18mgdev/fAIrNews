import m_20minutos, m_abc, m_cope, m_elconfidencial, sm_elpais, m_lasexta
import html2text

all_items = []
for e in m_20minutos.get_news_list():
    all_items.append(e)
for e in m_abc.get_news_list():
    all_items.append(e)
for e in m_cope.get_news_list():
    all_items.append(e)
for e in m_elconfidencial.get_news_list():
    all_items.append(e)
for e in sm_elpais.get_news_list():
    all_items.append(e)
for e in m_lasexta.get_news_list():
    all_items.append(e)



# soup=BeautifulSoup(get_news_JSON(rss2json.RRS2JSON+RSS_URL)[0]["content"])
# text=soup.get_text()
    

#sacar categorias

# print(len(all_items))
# for e in all_items:
#     for i in e["categories"]:
#         print(i)
    
print(len(all_items))

print(all_items[3]["title"])
print(all_items[3]["content"])

import keybert

kw_model = keybert.KeyBERT()

#topics, probs = topic_model.fit_transform([e["content"] for e in all_items])
kw = kw_model.extract_keywords(all_items[3]["content"])

print("palabras clave del contenido: ", kw)
kw = kw_model.extract_keywords(all_items[3]["title"])

print("palabras clave del título: ", kw)
print("categorias: ",all_items[3]["categories"])

"""
una buena manera para establecer las categorias de una noticia es sacar las kw del content y del titulo y sacar las que coincidan
"""