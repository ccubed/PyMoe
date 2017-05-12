import requests


class ALibrary:
    def __init__(self, readonly, settings):
        self.settings = settings
        self.rl = readonly
        
    