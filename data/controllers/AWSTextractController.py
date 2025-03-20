import boto3
import requests
from io import BytesIO
import json
import os

class AWSTextractController:

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

    def image_to_text(self, images_array):
        self._initialise()
        session = boto3.Session(
            aws_access_key_id = self.access_key_id,
            aws_secret_access_key = self.secret_access_key,
            region_name = self.region
        )

        results = []

        #for i, img_url in enumerate(images_array, start = 1):
        #    try:
        #        img_url = img_url[1] if isinstance(img_url, tuple) else img_url
        #        response = requests.get(img_url)
        #        image_bytes = BytesIO(response.content)
        #        textextract = session.client("textract")
        #        response = textextract.detect_document_text(
        #            Document={"Bytes": image_bytes.getvalue()}
        #        )
        #        extracted_text = ([block["Text"] for block in response["Blocks"] if block["BlockType"] == "LINE"])

        #        if extracted_text:
        #            results.append({
        #                "name": f"image{i:02}",  # Genera nombres como image01, image02...
        #                "text": extracted_text
        #            })

        #    except Exception:
        #        pass

        #json_output = json.dumps(results, indent=4, ensure_ascii=False)

        #with open("output.json", "w", encoding="utf-8") as json_file:
        #    json_file.write(json_output)

        return os.path.abspath("output.json")
