import os
import boto3
import shutil

from data.controllers.contracts.StorageController import StorageController
from domain.model.StorageInfo import StorageInfo

TEMPORAL_DIR = "temporal"
FILE_NAME = "markdown"
#TEMPORAL_PATH = f"{TEMPORAL_DIR}/temporal_results.txt"
BUCKET_NAME = "criptana-ai-crawler-info"
S3_FILE = "markdown"
IMAGES_FILE = "images.json"

class AWSStorageController(StorageController):

    def __init__(self):
        self.access_key_id = None
        self.secret_access_key = None
        self.region = None

    def _initialise(self):
        access_key_id = input("Access Key Id: ")
        secret_access_key = input("Secret Access Key: ")
        region = input("Region Name: ")
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
        self.region = region

    def _temporal_storage(self, results):
        os.makedirs(TEMPORAL_DIR, exist_ok=True)

        for i, part in enumerate(results, start=1):  # Recorrer cada parte del array
            file_name = f"{TEMPORAL_DIR}/{FILE_NAME}_{i}.md"  # Nombre del archivo
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(str(part))
        return os.path.getsize(TEMPORAL_DIR)

    def _delete_temporal_storage(self):
        shutil.rmtree(TEMPORAL_DIR)

    def store(self, results, images_path):
        self._initialise()
        temporal_size = self._temporal_storage(results)
        file_name = input("File name: ")
        s3_path = self.aws_upload(file_name, images_path)
        self._delete_temporal_storage()
        return StorageInfo(s3_path, temporal_size / 1024)

    def aws_upload(self, file_name, images_path):
        session = boto3.Session(
            aws_access_key_id = self.access_key_id,
            aws_secret_access_key = self.secret_access_key,
            region_name = self.region
        )
        s3 = session.client("s3")

        i = 0
        s3_name = file_name
        for markdown in os.listdir(TEMPORAL_DIR):
            if (i % 100 == 0):
                s3_name = f"{file_name}_{i}"
                print(s3_name)
            full_markdown_path = os.path.join(TEMPORAL_DIR, markdown)  # Get full path
            s3.upload_file(full_markdown_path, BUCKET_NAME, f"{s3_name}/markdown/{markdown}")
            i += 1

        s3.upload_file(images_path, BUCKET_NAME, f"{s3_name}/{IMAGES_FILE}")

        return f"s3://{BUCKET_NAME}/{s3_name}"
