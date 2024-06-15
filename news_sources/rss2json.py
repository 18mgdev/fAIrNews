import feedparser

def get_JSON(rss_url:str, items_limit=30):
    try:
        # Parsear el RSS
        feed = feedparser.parse(rss_url, agent='XYZ/3.0')
        
        # Extraer los elementos "item"
        items = []
        for entry in feed.entries:
            content=""
            if 'content' in entry and (len(entry.content)>0 and len(entry.content[0].value)>len(entry.summary)):
                content=entry.content[0].value
            else:
                content=entry.summary
            

            item = {
                'title': entry.title,
                'link': entry.link,
                'content': content,
                'pubDate': entry.published
            }
            if 'media_content' in entry and len(entry.media_content)>0:
                type_media=entry.media_content[0]['type'] if 'type' in entry.media_content[0] else "image"
                item['enclosure'] ={"link":entry.media_content[0]['url'],
                                    "type":type_media
                                    }
            elif "enclosure" in entry and len(entry.enclosure)>0:
                type_media=entry.enclosure[0].type if 'type' in entry.enclosure[0] else "image"
                item['enclosure'] ={"link":entry.enclosure[0].href,
                                    "type":type_media
                                    }
            items.append(item)
            if len(items)>=items_limit:
                break
        
        # Convertir la lista de diccionarios a JSON
        #json_output = json.dumps(items, indent=4)
        return items
    except:
        return []