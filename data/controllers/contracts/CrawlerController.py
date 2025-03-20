from abc import abstractmethod, ABC


class CrawlerController(ABC):

    @abstractmethod
    def crawl(self, url, white_list):
        pass