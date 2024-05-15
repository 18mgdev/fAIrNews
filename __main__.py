from news_collector import get_all_news
all_items=get_all_news()
print("num noticias: ",len(all_items))

from clusterizer import generate_top_keywords, cluster_news
top_keywords = generate_top_keywords(all_items, num_topics=4)

clustered_news = cluster_news(all_items, num_clusters=6)



from summarizer import summarize_headlines, summarize_articles


def generate_summs_json(all_items:list, top_keywords:list, min_rank_keyword=3):
    """
    Genera lista de resumenes en formato JSON
    """
    final_summs = []
    for keyword, rank in top_keywords:
        if rank < min_rank_keyword:
            break
        titles = []
        contents = []
        referencias=[]
        imagenes=[]
        index=0
        while index<len(all_items) and len(titles) < rank:
            noticia = all_items[index]
            if keyword in noticia["keywords"]: #dentro se mete la noticia
                titles.append(noticia["title"])
                contents.append(noticia["content"])
                referencias.append({
                    "title": noticia["title"],
                    "link": noticia["link"],
                    "source": noticia["medio"],
                    "keywords": noticia["keywords"]
                })
                if "enclosure" in noticia and noticia["enclosure"]!={} and "link" in noticia["enclosure"]:
                    imagenes.append({
                        "link": noticia["enclosure"]["link"]
                    })
                elif "enclosure" in noticia and noticia["enclosure"]!={} and "thumbnail" in noticia["enclosure"]:
                    imagenes.append({
                        "link": noticia["enclosure"]["thumbnail"]
                    })
            index+=1

        #se monta el json y se añade a la lista final
        final_summs.append(
            {
                "keyword": keyword,
                "relevance": rank,
                "title": summarize_headlines(titles).split(".")[0] if len(summarize_headlines(titles).split("."))>0 else summarize_headlines(titles),
                "summary": summarize_articles(contents),
                "references": referencias,
                "media": imagenes
            }
            )
    return final_summs
    
final_summs=generate_summs_json(all_items, top_keywords, min_rank_keyword=3)

import json
# with open("pruebas/noticias.json", "r", encoding="utf-8") as f:
#     all_items=json.load(f)



org_json=[]
for k in top_keywords:
    item={}
    item["keyword"]=k[0]
    item["noticias"]=[]
    for e in all_items:
        if k[0] in e["keywords"]:
            item["noticias"].append(e)
    org_json.append(item)
with open("pruebas/org_noticias.json", "w", encoding="utf-8") as f:
    json.dump(org_json, f, indent=4, ensure_ascii=False)



for e in top_keywords:
    print(e) if e[1]>1 else None



with open("pruebas/summs2.json", "w", encoding="utf-8") as f:
    json.dump(final_summs, f, indent=4, ensure_ascii=False)



