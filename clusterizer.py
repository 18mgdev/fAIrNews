from sklearn.feature_extraction.text import TfidfVectorizer
from text_cleaner import clean_text, remove_stop_words

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
    (indice, lista de json)
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
