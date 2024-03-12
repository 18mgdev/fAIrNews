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

print(all_items[0]["title"])
print(all_items[0]["content"])
