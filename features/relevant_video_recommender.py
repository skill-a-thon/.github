import scrapetube
searchkey= input("What would you like to learn about? ")
videos = scrapetube.get_search(searchkey,sort_by="relevance",limit=5)

for video in videos:
    print("https://www.youtube.com/watch?v=%s"% video['videoId'])
