from abc import abstractmethod, ABC


class StorageController(ABC):

    @abstractmethod
    def store(self, results, images_path):
        pass