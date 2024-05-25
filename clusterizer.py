from sklearn.feature_extraction.text import TfidfVectorizer
from text_preprocessor import clean_text, remove_stop_words

from collections import defaultdict # Utilizar defaultdict para manejar contadores automáticamente

def generate_top_keywords(all_items, num_topics=4):
    """
    Genera palabras clave en el campo ['keywords'] para cada noticia en all_items y devuelve un TOP de las palabras clave más frecuentes (dict)
    """
    all_texts = [remove_stop_words(clean_text(item["title"] + " " + item["content"])) for item in all_items]
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(all_texts)
    feature_names = tfidf_vectorizer.get_feature_names_out()
    
    all_keywords = defaultdict(int)
    for idx, item in enumerate(all_items):
        feature_index = tfidf_matrix[idx,:].nonzero()[1]
        tfidf_scores = zip(feature_index, [tfidf_matrix[idx, x] for x in feature_index])
        sorted_items = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)[:num_topics]
        keywords = [feature_names[i] for i, score in sorted_items]
        item['keywords'] = keywords
        for keyword in keywords:
            all_keywords[keyword] += 1

    sorted_keywords = sorted(all_keywords.items(), key=lambda x: x[1], reverse=True)
    return sorted_keywords


from sklearn.cluster import KMeans

def cluster_news(all_items, num_clusters=5):
    """
    Recibe la lista de JSONs de noticias y devuelve un diccionario con las noticias agrupadas por cluster.
    defaultdict[indice, lista de json]
    """
    # Preparar los textos de las noticias
    all_texts = [remove_stop_words(clean_text(item["title"] + " " + item["content"])) for item in all_items]
    
    # Crear la matriz TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(all_texts)
    
    # Aplicar K-means
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    clusters = kmeans.fit_predict(tfidf_matrix)
    
    # Asignar el cluster a cada noticia
    for idx, item in enumerate(all_items):
        item['cluster'] = clusters[idx]

    # Agrupar noticias por cluster
    clustered_news = defaultdict(list)
    for item in all_items:
        clustered_news[item['cluster']].append(item)
    
    return clustered_news



from sentence_transformers import SentenceTransformer

from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
def optimalK_silhouette(lista_textos, max_clusters, mostrar_grafico=False):
    """
    Encuentra el número óptimo de clusters utilizando el coeficiente de silueta.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(lista_textos)

    silhouette_scores = []
    ks = range(2, max_clusters)  # k = 1 no es válido para el coeficiente de silueta
    for k in ks:
        kmeans = KMeans(n_clusters=k, random_state=42)
        cluster_labels = kmeans.fit_predict(embeddings)
        silhouette_scores.append(silhouette_score(embeddings, cluster_labels))

    # Graficar los puntajes de silueta
    if mostrar_grafico:
        plt.figure(figsize=(8, 4))
        plt.plot(ks, silhouette_scores, '-o')
        plt.xlabel('number of clusters, k')
        plt.ylabel('silhouette score')
        plt.title('Silhouette Analysis For Optimal k')
        plt.xticks(ks)
        plt.show()
    return silhouette_scores.index(max(silhouette_scores))+2




def get_classified_news_list(top_keywords:defaultdict, clusters:defaultdict, ln:list):
    """
    Devuelve la lista de agrupaciones de NOTICIAS RELACIONADAS clasificadas por keyword y cluster
    {
        "keyword": str,
        "noticias": list[noticia1, noticia2, ...]
    }
    """
    #agrupo las noticias por keyword
    org_json=[]
    for k in top_keywords:
        item={}
        item["keyword"]=k[0]
        item["noticias"]=[]
        for e in ln:
            if k[0] in e["keywords"]:
                item["noticias"].append(e)
        org_json.append(item)

    #selecciono las noticias solo si coinciden en el keyword y en el cluster
    for e in org_json:
        top=defaultdict(int)
        for c in e["noticias"]:
            top[c["cluster"]]+=1
        if len(top)>0:
            st = sorted(top.items(), key=lambda x: x[1], reverse=True)
            cluster_num=int(st[0][0])

            clusters[cluster_num]
            selected_ids=defaultdict(int)
            for noticia in e["noticias"]+clusters[cluster_num]:
                selected_ids[noticia["id"]]+=1
            
            noticias_escogidas=[]
            for noti in e["noticias"]:
                if selected_ids[noti["id"]]==2 and ln[noti["id"]-1]!=None:
                    noticias_escogidas.append(ln[noti["id"]-1])
                    ln[noti["id"]-1]=None
            e["noticias"]=noticias_escogidas

    return sorted(org_json, key=lambda x: len(x["noticias"]), reverse=True)