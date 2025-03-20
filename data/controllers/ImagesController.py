import re
import requests

class ImagesController:

    def download_images(self, image_url):
        try:
            return requests.get(image_url).content
        except Exception as e:
            print(f"Failed to download {image_url}: {e}")