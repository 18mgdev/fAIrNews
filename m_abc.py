import functions as f
import api_rss2json as r2j

RSS_URL="https://www.abc.es/rss/2.0/portada/"
#RSS_URL="https://www.abc.es/rss/2.0/ultima-hora/"

#

def get_news_list():
    """
    Get news from abc and return it as a JSON OBJECT list
    """
    items = r2j.get_JSON(RSS_URL)["items"]
    for e in items:
        e["content"]=f.html_to_text(e["description"])
    return items