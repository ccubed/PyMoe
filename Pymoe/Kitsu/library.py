import requests
from ..errors import *

class KitsuLib:
    def __init__(self, api, header):
        self.apiurl = api
        self.header = header