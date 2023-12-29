class NewsModel:
    def __init__(self, news):
        self.headline = news['title']
        self.brief = news['description']
