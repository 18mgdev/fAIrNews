from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime
import random

def get_database():
 
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://miguelgonzalez72:0rX7jez6iYG027cS@cluster0.31g1g5x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    # Cree una conexión con MongoClient. Puede importar MongoClient o usar pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Cree la base de datos para nuestro ejemplo (usaremos la misma base de datos en todo el tutorial
    return client['tfg']

def insert_noticia(db:MongoClient,noticia):
    """
    Inserta una noticia en la base de datos
    param noticia: JSON con la noticia ya formateada
    Retorna el id de la noticia insertada
    """

    # Insertar noticia
    
    return db.get_collection("noticias").insert_one(noticia).inserted_id

def insert_portada(db:MongoClient,portada):
    """
    Inserta una portada en la base de datos
    param portada: JSON con la portada ya formateada
    """
    # Insertar portada
    db.get_collection("portada").insert_one(portada)

    return True

def get_noticia(id:str):
    """
    Devuelve una noticia de la base de datos
    param id: id de la noticia
    """
    # Establecer la conexión con la base de datos
    db = get_database()
    # Devolver noticia
    return db.get_collection("noticias").find_one({"_id":ObjectId(id)})

def get_ultima_portada():
    # Establecer la conexión con la base de datos
    db = get_database()
    # Devolver portada
    return db.get_collection("portada").find_one(sort=[('date', -1)])

def insertar_noticias(noticias:list, num_noticias_capturadas, num_keywords, num_medios,num_noticias_generadas):
    """
    Inserta una lista de noticias en NOTICIAS y crea la portada en PORTADA en la base de datos
    param noticias: lista de JSON con las noticias ya formateadas
    """
    db=get_database()
    fecha=datetime.datetime.now()
    # Insertar noticias
    noticias_portada=[]
    for e in noticias:
        thumbnail=select_imagen_portada(e["media"])
        noticia={
            "date": fecha,
            "keyword": e["keyword"],
            "relevance": e["relevance"],
            "title": e["title"].capitalize(),
            "summary": e["summary"],
            "references": e["references"],
            "media": e["media"],
            "thumbnail": thumbnail
        }
        id=insert_noticia(db,noticia)
        noticias_portada.append({
            "date": fecha,
            "noticia_id": id,
            "relevance": e["relevance"],
            "keyword": e["keyword"],
            "title": e["title"].capitalize(),
            "brief_summary": e["summary"].split(".")[0]+"..." if len(e["summary"].split("."))>0 else e["summary"],
            "thumbnail": thumbnail
        })
    # Insertar portada
    portada={
        "date": fecha,
        "num_articles": num_noticias_capturadas,
        "num_keywords": num_keywords,
        "num_generated_articles": num_noticias_generadas,
        "num_sources": num_medios,
        "noticias": noticias_portada
    }
    insert_portada(db,portada)
    return True

def select_imagen_portada(items:list):
    # Filtrar los elementos que tienen "image" en su campo "type"
    image_items = [item for item in items if 'image' in item['type']]
    
    if not image_items:
        return ""
    
    # Seleccionar aleatoriamente uno de los elementos filtrados
    selected_item = random.choice(image_items)
    
    # Devolver el campo "link" del elemento seleccionado
    return selected_item['link']

# Esto se agrega para que muchos archivos pueden reutilizar la función get_database()
if __name__ == "__main__":   
    print("activo")
    