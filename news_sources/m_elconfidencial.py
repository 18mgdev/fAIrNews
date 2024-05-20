import text_cleaner as f
import api_rss2json as r2j

RSS_URL="https://rss.elconfidencial.com/espana/"
NAME="ElConfidencial"

#

def get_news_list():
    """
    Get news from elconfidencial and return it as a JSON OBJECT list
    """
    items = r2j.get_JSON(RSS_URL)["items"]
    for e in items:
        e["medio"]=NAME
        e["title"]=f.rss_clean_html(e["title"])
        e["content"]=f.rss_clean_html(e["content"])
    return items