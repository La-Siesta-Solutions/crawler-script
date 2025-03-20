from data.CrawlerRepository import CrawlerRepository
from data.controllers.DownloadImagesController import DownloadImagesController
from data.controllers.SpiderController import SpiderController
from domain.CrawlerInteractor import CrawlerInteractor
from domain.DownloadImagesInteractor import DownloadImagesInteractor
from domain.StoreInteractor import StoreInteractor
from domain.model.StorageType import StorageType


def crawl():
    api_key = input("Enter the Spider api-key: ")
    url = input("Enter the url to crawl: ")
    white_list = input("Do you want to white-list? Separate it by comas or leave it blank: ")
    white_list_curated = [item.strip() for item in white_list.split(",")]

    crawler_controller = SpiderController(api_key)
    crawler_repository = CrawlerRepository(crawler_controller)
    crawler_interactor = CrawlerInteractor(crawler_repository)
    print("Crawling " + url + "...")
    return crawler_interactor.get_info(url, white_list_curated)


def download_images(crawl_content):
    download_images_controller = DownloadImagesController()
    download_images_interactor = DownloadImagesInteractor(download_images_controller)
    return download_images_interactor.download_images(crawl_content)

def clean_images():
    download_images_controller = DownloadImagesController()
    download_images_interactor = DownloadImagesInteractor(download_images_controller)
    return download_images_interactor.clean_images_storage()

def store(crawl_content, images_path):
    storage_option = input("Where do you want to store the results?\n[1] Local\n[2] Amazon S3\n")
    if storage_option == str(1):
        storage_type = StorageType.LOCAL
    else:
        storage_type = StorageType.AWS
    store_interactor = StoreInteractor(crawl_content, storage_type)

    return store_interactor.store(images_path)

if __name__ == "__main__":
    print("")
    print("-------------------")
    print(" LA SIESTA CRAWLER")
    print("-------------------")
    print("")
    crawl_results = crawl()
    print("")
    print("----------------------------------------------------------")
    print("Crawl completed! Total cost: " + str(crawl_results.price))
    print("----------------------------------------------------------")
    print("")
    images_path = download_images(crawl_results.all_content)
    if images_path is not None:
        print("")
        print("----------------------------------------------------------")
        print("Images downloaded at\n" + str(images_path))
        print("----------------------------------------------------------")
        print("")
    store_results = store(crawl_results.all_content, images_path)
    print("")
    print("----------------------------------------------------------")
    print(f"Storage completed! {store_results.size:.2f} KB processed into \n{store_results.path}")
    print("----------------------------------------------------------")
    print("")
    #clean_images()
