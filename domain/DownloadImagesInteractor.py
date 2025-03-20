from data.controllers.DownloadImagesController import DownloadImagesController
from data.controllers.AWSTextractController import AWSTextractController


class DownloadImagesInteractor:

    def __init__(self, images_controller: DownloadImagesController):
        self.images_controller = images_controller
        self.textextract_controller = AWSTextractController()

    def download_images(self, results):
        images_url = self.images_controller.extract_images(results)
        storage_option = input(f"We have found {len(images_url)} images.\n"
                               f"Would you like to process them? [Y][N]...")
        if storage_option == "Y" or storage_option == "y":
            return self.textextract_controller.image_to_text(images_url)
            #self.store_results(json_response)
        return None

    def storage_result(self, json_response):
        print("")

    def clean_images_storage(self):
        self.images_controller.clean_temporal_storage()
