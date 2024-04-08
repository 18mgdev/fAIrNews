import functions as f
import api_rss2json as r2j

RSS_URL="https://www.lasexta.com/rss/351410.xml"

#

def get_news_list():
    """
    Get news from lasexta and return it as a JSON OBJECT list
    """
    items = r2j.get_JSON(RSS_URL)["items"]
    for e in items:
        e["content"]=f.clean_html(e["content"])
    return items