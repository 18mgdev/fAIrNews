import functions as f
import api_rss2json as r2j

RSS_URL="https://www.cope.es/api/es/news/rss.xml"

#

def get_news_list():
    """
    Get news from cope and return it as a JSON OBJECT list
    """
    items = r2j.get_JSON(RSS_URL)["items"]
    for e in items:
        e["content"]=f.clean_html(e["description"])
    return items