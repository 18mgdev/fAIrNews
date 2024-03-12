import functions as f
import api_rss2json as r2j

RSS_URL="https://rss.elconfidencial.com/espana/"

#

def get_news_list():
    """
    Get news from elconfidencial and return it as a JSON OBJECT list
    """
    items = r2j.get_JSON(RSS_URL)["items"]
    for e in items:
        e["content"]=f.html_to_text(e["content"])
    return items