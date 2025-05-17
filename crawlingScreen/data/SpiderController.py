from spider import Spider

class SpiderController():

    def __init__(self, api_key):
        self.app = Spider(api_key=api_key)

    def crawl(self, url, white_list):
        crawler_params = {
            'limit': 400,
            'proxy_enabled': True,
            'store_data': False,
            'metadata': True,
            'request': 'smart',
            'return_format': 'markdown',
            'readability': True,
            'full_resources': True,
            'whitelist': white_list
        }
        return self.app.crawl_url(url, params=crawler_params)
