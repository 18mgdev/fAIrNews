#1 coger noticias
from news_collector import get_all_news
all_items=get_all_news()
import json
print("num noticias: ",len(all_items))
with open("pruebas/news.json", "w", encoding="utf-8") as f:
    json.dump(all_items, f, indent=4, ensure_ascii=False)


#2 generar top keywords y clusters
from clusterizer import generate_top_keywords, cluster_news, optimalK_silhouette, get_classified_news_list
all_texts=[]
for e in all_items:
    all_texts.append(e["title"]+". "+e["content"])
k_optimal=optimalK_silhouette(all_texts, int(len(all_items)*0.8))

clustered_news = cluster_news(all_items, num_clusters=k_optimal)

top_keywords = generate_top_keywords(all_items, num_topics=4)

#3 crear lista de noticias agrupadas por keywords y clusters
classified_news=get_classified_news_list(top_keywords, clustered_news, all_items)


# import json
# import numpy as np

# def convert_to_serializable(obj):
#     if isinstance(obj, dict):
#         return {k: convert_to_serializable(v) for k, v in obj.items()}
#     elif isinstance(obj, list):
#         return [convert_to_serializable(i) for i in obj]
#     elif isinstance(obj, np.int32):
#         return int(obj)
#     else:
#         return obj

# # Convierte classified_news a una estructura serializable
# classified_news_serializable = convert_to_serializable(classified_news)

# with open("pruebas/resultado.json", "w", encoding="utf-8") as f:
#     json.dump(classified_news_serializable, f, indent=4, ensure_ascii=False)





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



