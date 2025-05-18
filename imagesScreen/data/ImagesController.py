import os
import re
import requests

from core.domain.model.CrawlResult import CrawlResult

TEMPORAL_RESULTS_STORAGE = "temp_results.txt"

class ImagesController:

    @staticmethod
    def __temporal_results_storage(results):
        with open(str(TEMPORAL_RESULTS_STORAGE), "w") as f:
            f.write(str(results))

    @staticmethod
    def __temporal_results_delete():
        os.remove(TEMPORAL_RESULTS_STORAGE)

    def extract_images_url(self, results: CrawlResult):
        self.__temporal_results_storage(results.all_content)
        with open(TEMPORAL_RESULTS_STORAGE, "r", encoding="utf-8") as file:
            markdown_content = file.read()
        self.__temporal_results_delete()
        return re.findall(r"!\[.*?\]\((https?://.*?)\)", markdown_content)
