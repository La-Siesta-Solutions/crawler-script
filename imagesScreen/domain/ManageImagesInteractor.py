from core.domain.model.CrawlResult import CrawlResult
from imagesScreen.data.AWSTextractController import AWSTextractController
from imagesScreen.data.ImagesController import ImagesController
from imagesScreen.domain.contract.ImagesScreen import ImagesScreen
import os
import json


IMAGES_CONTENT_STORAGE = "images_content.json"

class ManageImagesInteractor:

    def __init__(self, images_screen: ImagesScreen, images_controller: ImagesController,
                 aws_text_extract: AWSTextractController):
        self.images_screen = images_screen
        self.images_controller = images_controller
        self.aws_text_extract = aws_text_extract

    def __manage_user_input(self, user_input, images_url_list):
        if user_input == "Y" or user_input == "y":
            amazon_access_key = self.images_screen.ask_amazon_access_key()
            amazon_secret_key = self.images_screen.ask_amazon_secret_key()
            amazon_region = self.images_screen.ask_amazon_region_name()
            self.images_screen.show_images_processing_disclaimer(images_url_list)
            self.aws_text_extract.initialise(amazon_access_key, amazon_secret_key, amazon_region)
            content_images_json = self.aws_text_extract.image_to_text(images_url_list)
            self.images_screen.show_processing_result(images_url_list, len(json.loads(content_images_json)))
            return content_images_json
        return None

    #@staticmethod
    #def __storage_images_content(images_content_json):
    #    with open(IMAGES_CONTENT_STORAGE, "w", encoding="utf-8") as json_file:
    #        json_file.write(images_content_json)
    #    return os.path.abspath(IMAGES_CONTENT_STORAGE)


    def manage_images(self, results: CrawlResult):
        self.images_screen.show_title()
        images_url_list = self.images_controller.extract_images_url(results)
        user_input = self.images_screen.show_images_text(images_url_list)
        return self.__manage_user_input(user_input, images_url_list)

