from abc import ABC, abstractmethod


class ImagesScreen(ABC):

    @abstractmethod
    def show_title(self):
        pass

    @abstractmethod
    def show_images_text(self, images_amount):
        pass

    @abstractmethod
    def ask_amazon_access_key(self):
        pass

    @abstractmethod
    def ask_amazon_secret_key(self):
        pass

    @abstractmethod
    def ask_amazon_region_name(self):
        pass

    @abstractmethod
    def show_images_processing_disclaimer(self, images_amount):
        pass

    @abstractmethod
    def show_processing_result(self, images_amount, images_processed):
        pass