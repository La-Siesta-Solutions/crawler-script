from crawlingScreen.data.CrawlerRepository import CrawlerRepository
from crawlingScreen.data.SpiderController import SpiderController
from crawlingScreen.domain.contract.CrawlingView import CrawlingView
from crawlingScreen.domain.model.CrawlResult import CrawlResult


class CrawlerInteractor:

    def __init__(self, crawling_view: CrawlingView):
        self.crawler_repository: CrawlerRepository = None
        self.crawling_view = crawling_view

    def __init_repository(self):
        api_key = self.crawling_view.ask_client_api_key()
        spider_controller = SpiderController(api_key)
        self.crawler_repository = CrawlerRepository(spider_controller)

    def __get_info_from_url(self):
        url = self.crawling_view.ask_url_to_crawl()
        white_list = self.crawling_view.ask_white_list()
        white_list_curated = [item.strip() for item in white_list.split(",")]
        self.crawling_view.show_crawling(url)
        return self.crawler_repository.get_info(url, white_list_curated)

    def crawl(self):
        self.crawling_view.show_title()
        self.__init_repository()
        results: CrawlResult = self.__get_info_from_url()
        self.crawling_view.show_costs(results.price)


