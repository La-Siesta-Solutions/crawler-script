from data.CrawlerRepository import CrawlerRepository

class CrawlerInteractor:

    def __init__(self, crawler_repository: CrawlerRepository):
        self.crawler_repository = crawler_repository

    def get_info(self, url, white_list):
        return self.crawler_repository.get_info(url, white_list)
