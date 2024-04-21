from eventregistry import *
er = EventRegistry(apiKey = "78cd25d3-b69f-406d-bc75-6fe0371a1a09")

recentQ = GetRecentArticles(er, returnInfo = ReturnInfo(ArticleInfoFlags(concepts = True, categories = True)))

starttime = time.time()
while True:
    articleList = recentQ.getUpdates()
    print("%d articles were added since the last call" % len(articleList))

    for article in articleList:
        print(article)

    print("sleeping for 60 seconds...")
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
                