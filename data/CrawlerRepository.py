from data.controllers.contracts.CrawlerController import CrawlerController
from domain.model.CrawlResult import CrawlResult

class CrawlerRepository:

    def __init__(self, spider_controller: CrawlerController):
        self.storage_controller = None
        self.spider_controller = spider_controller

    def get_info(self, url, white_list):
        results = self.spider_controller.crawl(url, white_list)
        return self.build_results(results)

    def build_results(self, results):
        if isinstance(results, list) and len(results) > 0:
            response_data = results[0]
            return CrawlResult(results, response_data.get("costs", {}).get("total_cost", 0))
        else:
            return None

