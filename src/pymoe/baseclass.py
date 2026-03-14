from abc import ABC, abstractmethod

class BaseAPI(ABC):
    def __init__(self, web_client, base_url):
        self.web_client = web_client
        self.base_url = base_url

    @abstractmethod
    def _get(self, **kwargs):
        pass

    @abstractmethod
    def _post(self, **kwargs):
        pass

    def _merge_headers(self, custom_headers = None):
        if custom_headers:
            return self.web_client.headers.copy().update(custom_headers)
        else:
            return self.web_client.headers
