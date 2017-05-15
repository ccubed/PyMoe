import json
import requests

class AGet:
    def __init__(self, readonly, settings):
        self.settings = settings
        self.rl = readonly
        self.mapping = {
            'anime': self.__anime, 'manga': self.__manga,
            'staff': self.__staff, 'studio': self.__studio,
            'character': self.__character
        }

    def get(self, ttype, item_id):
        """
        This is a universal function. It's the only function this class
        publically exposes. It serves as the work horse for the rest of this
        classes uses. You need only pass a type and the id. This class and
        this function will handle the rest behind the scenes. This is not used
        for reviews.

        :param str ttype: One of anime, manga, staff, studio, character
        :param int item_id: The Item ID
        """
        if ttype in self.mapping:
            return self.mapping[ttype](item_id)
        else:
            raise SyntaxError(
                "{} is not an accepted type. Should be one of: {}".format(ttype, ", ".join(self.mapping.keys())))

    def __anime(self, item_id):
        """
        The internal function to retrieve an anime's details.

        :param int item_id: the anime's ID
        :return: dict or None
        :rtype: dict or NoneType
        """
        r = requests.get(self.settings['apiurl'] + "anime/{}".format(item_id),
                         params={'access_token': self.rl()},
                         headers=self.settings['header'])
        jsd = r.text

        # AniList can return a newline for no results for some reason
        if jsd == '\n' or r.status_code == 404:
            return None
        else:
            jsd = json.loads(jsd)
            if 'error' in jsd:
                # it can also return a json error
                return None
            else:
                return jsd

    def __manga(self, item_id):
        """
        The internal function to retrieve an anime's details.

        :param int item_id: the anime's ID
        :return: dict or None
        :rtype: dict or NoneType
        """
        r = requests.get(self.settings['apiurl'] + "manga/{}".format(item_id),
                         params={'access_token': self.rl()},
                         headers=self.settings['header'])
        jsd = r.text

        # AniList can return a newline for no results for some reason
        if jsd == '\n' or r.status_code == 404:
            return None
        else:
            jsd = json.loads(jsd)
            if 'error' in jsd:
                # it can also return a json error
                return None
            else:
                return jsd

    def __staff(self, item_id):
        """
        The internal function to retrieve a manga's details.

        :param int item_id: the anime's ID
        :return: dict or None
        :rtype: dict or NoneType
        """
        r = requests.get(self.settings['apiurl'] + "anime/{}".format(item_id),
                         params={'access_token': self.rl()},
                         headers=self.settings['header'])
        jsd = r.text

        # AniList can return a newline for no results for some reason
        if jsd == '\n' or r.status_code == 404:
            return None
        else:
            jsd = json.loads(jsd)
            if 'error' in jsd:
                # it can also return a json error
                return None
            else:
                return jsd

    def __studio(self, item_id):
        """
        The internal function to retrieve a studio's details.

        :param int item_id: the anime's ID
        :return: dict or None
        :rtype: dict or NoneType
        """
        r = requests.get(self.settings['apiurl'] + "studio/{}".format(item_id),
                         params={'access_token': self.rl()},
                         headers=self.settings['header'])
        jsd = r.text

        # AniList can return a newline for no results for some reason
        if jsd == '\n' or r.status_code == 404:
            return None
        else:
            jsd = json.loads(jsd)
            if 'error' in jsd:
                # it can also return a json error
                return None
            else:
                return jsd

    def __character(self, item_id):
        """
        The internal function to retrieve a character's details.

        :param int item_id: the anime's ID
        :return: dict or None
        :rtype: dict or NoneType
        """
        r = requests.get(self.settings['apiurl'] + "character/{}".format(item_id),
                         params={'access_token': self.rl()},
                         headers=self.settings['header'])
        jsd = r.text

        # AniList can return a newline for no results for some reason
        if jsd == '\n' or r.status_code == 404:
            return None
        else:
            jsd = json.loads(jsd)
            if 'error' in jsd:
                # it can also return a json error
                return None
            else:
                return jsd

    def get_reviews(self, item_id, item_type, get_all=True, review_id=None):
        """
        This function is used to get reviews. Reviews come in many shapes and sizes so it
        was unrealistic to stick them all in get and try to work that function that way.
        A review needs to know if it's attached to a user, anime or manga and then if
        you want all of the reviews for that item or just one.
        Note: For users, there is no filter, so you will get a list of all the user's
        reviews regardless of what all is set to.

        :param item_id: The id of the item the review or reviews are associated with. If this is a user, it can be a name or id.
        :param str item_type: One of the following - anime, manga, user
        :param bool get_all: True if you want all of the reviews for the item or false if you want one review
        :param int review_id: If you specify false in all, you must provide a review ID
        :return: Depending, a list of dicts, a dict or None
        :rtype: dict, list or NoneType
        """
        if not get_all and not review_id:
            raise SyntaxError("You have to pass a review_id if you want a specific review.")
        else:
            if not get_all:
                if item_type == "user":
                    raise SyntaxError("User's can only return all their reviews.")
                else:
                    r = requests.get(self.settings['apiurl'] + "{}/review/{}".format(item_type, review_id),
                                     params={'access_token': self.rl()},
                                     headers=self.settings['header'])

                    jsd = r.text

                    if jsd == '\n' or r.status_code == 404:
                        return None
                    else:
                        jsd = json.loads(jsd)
                        if 'error' in jsd:
                            return None
                        else:
                            return jsd
            else:
                r = requests.get(self.settings['apiurl'] + "{}/{}/reviews".format(item_type, item_id),
                                 params={'access_token': {self.rl()}},
                                 headers=self.settings['header'])

                jsd = r.text

                if jsd == '\n' or r.status_code == 404:
                    return None
                else:
                    jsd = json.loads(jsd)
                    if 'error' in jsd:
                        return None
                    else:
                        return jsd
