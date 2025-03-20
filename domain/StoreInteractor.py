from data.controllers.AWSStorageController import AWSStorageController
from data.controllers.LocalStorageController import LocalStorageController
from domain.model.StorageType import StorageType

class StoreInteractor:

    def __init__(self, content, storage_type: StorageType):
        self.content = content
        self.storage_type = storage_type
        self.storage_controller = None

    def store(self, images_path):
        if self.storage_type == StorageType.LOCAL:
            self.storage_controller = LocalStorageController()
        elif self.storage_type == StorageType.AWS:
            self.storage_controller = AWSStorageController()

        return self.storage_controller.store(self.content, images_path)
