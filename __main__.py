MIN_RELEVANCE_SUMMARY_GENERATION = 2

import datetime
start_time=datetime.datetime.now()
#1 coger noticias
from news_collector import get_all_news
collector=get_all_news()
all_items=collector["items"]
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




#4 crea el json de las noticias resumidas
from summarizer import summarize_headlines, summarize_articles

def generate_summs_json(classification:list, top_keywords, min_rank_keyword=MIN_RELEVANCE_SUMMARY_GENERATION):
    """
    Genera lista de resumenes en formato JSON
    """
    final_summs = []
    for tema in classification:
        titles = []
        contents = []
        referencias=[]
        imagenes=[]
        relevance=0
        for k in top_keywords:
            if k[0] == tema["keyword"]:
                relevance=k[1]
                break
        if relevance<min_rank_keyword:
            break
        for noticia in tema["noticias"]:
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
                    "link": noticia["enclosure"]["link"],
                    "type": noticia["enclosure"]["type"] if "type" in noticia["enclosure"] else "image"
                })
            elif "enclosure" in noticia and noticia["enclosure"]!={} and "thumbnail" in noticia["enclosure"]:
                imagenes.append({
                    "link": noticia["enclosure"]["thumbnail"],
                    "type": noticia["enclosure"]["type"] if "type" in noticia["enclosure"] else "image"
                })
        #se monta el json y se añade a la lista final

        final_summs.append(
            {
                "keyword": tema["keyword"],
                "relevance": relevance,
                "title": summarize_headlines(titles).split(".")[0] if len(summarize_headlines(titles).split("."))>0 else summarize_headlines(titles),
                "summary": summarize_articles(contents),
                "references": referencias,
                "media": imagenes
            }
            )
    return final_summs
 
final_summs=generate_summs_json(classified_news, top_keywords)

#5 insertar noticias en la base de datos
from mongodb_functions import insertar_noticias
insertar_noticias(
    noticias=final_summs,
    num_noticias_capturadas=len(all_items),
    num_keywords=len(top_keywords),
    num_medios=collector["num_medios"],
    num_noticias_generadas=len(final_summs)
                  )


print(datetime.datetime.now()-start_time)