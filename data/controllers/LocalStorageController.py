import os
import shutil

from data.controllers.contracts.StorageController import StorageController
from domain.model.StorageInfo import StorageInfo

FILE_NAME = "markdown"

class LocalStorageController(StorageController):

    def store(self, results, images_path):
        folder_name = input("Folder Name: ")
        os.makedirs(folder_name, exist_ok=True)

        for i, part in enumerate(results, start=1):  # Recorrer cada parte del array
            file_name = f"{folder_name}/{FILE_NAME}_{i}.md"  # Nombre del archivo
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(str(part))  # Guardar la parte en el archivo

        images_size = self.__store_images(images_path, folder_name)
        return StorageInfo(os.path.abspath(f"{folder_name}"),
                           (os.path.getsize(f"{folder_name}") + images_size)/ 1024)

    def __store_images(self, images_path, destination):
        images_size = os.path.getsize(images_path)
        if images_path is not None:
            shutil.move(images_path, destination)
        return images_size
