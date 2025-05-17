from crawlingScreen.data.SpiderController import SpiderController
from crawlingScreen.domain.model.CrawlResult import CrawlResult

class CrawlerRepository:

    def __init__(self, spider_controller: SpiderController):
        self.storage_controller = None
        self.spider_controller = spider_controller

    @staticmethod
    def __build_results(results):
        if isinstance(results, list) and len(results) > 0:
            response_data = results[0]
            return CrawlResult(results, response_data.get("costs", {}).get("total_cost", 0))
        else:
            return None

    def get_info(self, url, white_list):
        results = self.spider_controller.crawl(url, white_list)
        return self.__build_results(results)



