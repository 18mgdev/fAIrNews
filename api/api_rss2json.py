import urllib.request
import json

RRS2JSON_API="https://api.rss2json.com/v1/api.json?rss_url="


def get_JSON(m_rss_url):
    """
    Get news from a RSS feed and return it as JSON
    """
    try:
        with urllib.request.urlopen(RRS2JSON_API+m_rss_url) as response:
            data = json.loads(response.read().decode())
            return data
    except:
        return {"items":[]}