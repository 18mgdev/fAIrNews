import functions as f
import api_rss2json as r2j

RSS_URL="https://www.elcorreo.com/rss/2.0/portada/"


def get_news_list():
    """
    Get news from elcorreo and return it as a JSON OBJECT list
    """
    items = r2j.get_JSON(RSS_URL)["items"]
    for e in items:
        e["content"]=f.clean_html(str(e["content"]))
    return items
print(get_news_list()[0]["content"])