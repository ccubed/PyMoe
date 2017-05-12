import json
import requests

class AGet:
    def __init__(self, readonly, settings):
        self.settings = settings
        self.rl = readonly
        self.mapping = {
            'anime': self.__anime, 'manga': self.__manga,
            'staff': self.__staff, 'studio': self.__studio,
            'character': self.__character, 'review': self.__review
        }
        
    def get(self, type, item_id):
        """
        This is a universal function. It's the only function this class
        publically exposes. It serves as the work horse for the rest of this
        classes uses. You need only pass a type and the id. This class and 
        this function will handle the rest behind the scenes.
        
        :param type str: One of anime, manga, staff, studio, character, review
        :param item_id int: The Item ID
        """
        pass
    
    def __anime(self, id):
        pass

    def __manga(self, id):
        pass
    
    def __staff(self, id):
        pass
    
    def __studio(self, id):
        pass
    
    def __character(self, id):
        pass
    
    def __review(self, id):
        pass