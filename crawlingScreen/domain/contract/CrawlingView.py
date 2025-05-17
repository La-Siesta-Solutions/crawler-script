from abc import ABC, abstractmethod


class CrawlingView(ABC):

    @abstractmethod
    def show_title(self):
        pass

    @abstractmethod
    def ask_client_api_key(self):
        pass

    @abstractmethod
    def ask_url_to_crawl(self):
        pass

    @abstractmethod
    def ask_white_list(self):
        pass

    @abstractmethod
    def show_crawling(self, url):
        pass

    @abstractmethod
    def show_costs(self, total_cost):
        pass