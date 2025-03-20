import os
import re
import shutil

import requests

TEMPORAL_RESULTS_STORAGE = "temp_results.txt"
TEMPORAL_IMAGES_STORAGE = "temp/images/"

class DownloadImagesController:

    def __temporal_results_storage(self, results):
        with open(str(TEMPORAL_RESULTS_STORAGE), "w") as f:
            f.write(str(results))

    def __temporal_results_delete(self):
        os.remove(TEMPORAL_RESULTS_STORAGE)

    #def __store_images(self, image_urls):
    #    os.makedirs(TEMPORAL_IMAGES_STORAGE, exist_ok=True)
    #    for idx, img_url in enumerate(image_urls):
    #        try:
    #            img_data = requests.get(img_url).content
    #            img_name = f"{TEMPORAL_IMAGES_STORAGE}image_{idx}.jpg"
    #            with open(img_name, "wb") as img_file:
    #                img_file.write(img_data)
    #        except Exception as e:
    #            print(f"Failed to download {img_url}: {e}")

    def extract_images(self, results):
        self.__temporal_results_storage(results)
        with open(TEMPORAL_RESULTS_STORAGE, "r", encoding="utf-8") as file:
            markdown_content = file.read()
        self.__temporal_results_delete()

        return re.findall(r"!\[.*?\]\((https?://.*?)\)", markdown_content)

        #storage_option = input(f"We have found {len(image_urls)} images.\n"
        #                       f"Would you like to process them? [Y][N]...")
        #if storage_option == "Y" or storage_option == "y":
            #self.__store_images(image_urls)
        #    return os.path.abspath(TEMPORAL_IMAGES_STORAGE)
        #return None

    #def clean_temporal_storage(self):
    #    shutil.rmtree("temp")
