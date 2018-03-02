import json
import requests

class AGet:
    def __init__(self, settings):
        self.settings = settings

    def anime(self, item_id):
        """
        The function to retrieve an anime's details.

        :param int item_id: the anime's ID
        :return: dict or None
        :rtype: dict or NoneType
        """
        query_string = """\
            query ($id: Int) {
                Media(id: $id, type: ANIME) {
                    title {
                        romaji
                        english
                    }
                    startDate {
                        year
                        month
                        day
                    }
                    endDate {
                        year
                        month
                        day
                    }
                    coverImage {
                        large
                    }
                    bannerImage
                    format
                    status
                    episodes
                    season
                    description
                    averageScore
                    meanScore
                    genres
                    synonyms
                    nextAiringEpisode {
                        airingAt
                        timeUntilAiring
                        episode
                    }
                }
            }
        """
        vars = {"id": item_id}
        r = requests.post(self.settings['apiurl'],
                         headers=self.settings['header'],
                         json={'query': query_string, 'variables': vars})
        jsd = r.text

        try:
            jsd = json.loads(jsd)
        except ValueError:
            return None
        else:
            return jsd

    def manga(self, item_id):
        """
        The function to retrieve an anime's details.

        :param int item_id: the anime's ID
        :return: dict or None
        :rtype: dict or NoneType
        """
        query_string = """\
            query ($id: Int) {
                Media(id: $id, type: MANGA) {
                    title {
                        romaji
                        english
                    }
                    startDate {
                        year
                        month
                        day
                    }
                    endDate {
                        year
                        month
                        day
                    }
                    coverImage {
                        large
                    }
                    bannerImage
                    format
                    chapters
                    volumes
                    status
                    description
                    averageScore
                    meanScore
                    genres
                    synonyms
                }
            }
        """
        vars = {"id": item_id}
        r = requests.post(self.settings['apiurl'],
                         headers=self.settings['header'],
                         json={'query': query_string, 'variables': vars})
        jsd = r.text

        try:
            jsd = json.loads(jsd)
        except ValueError:
            return None
        else:
            return jsd

    def staff(self, item_id):
        """
        The function to retrieve a manga's details.

        :param int item_id: the anime's ID
        :return: dict or None
        :rtype: dict or NoneType
        """
        query_string = """\
            query ($id: Int) {
                Staff(id: $id) {
                    name {
                        first
                        last
                        native
                    }
                    description
                    language
                }
            }
        """
        vars = {"id": item_id}
        r = requests.post(self.settings['apiurl'],
                          headers=self.settings['header'],
                          json={'query': query_string, 'variables': vars})
        jsd = r.text

        try:
            jsd = json.loads(jsd)
        except ValueError:
            return None
        else:
            return jsd

    def studio(self, item_id):
        """
        The function to retrieve a studio's details.

        :param int item_id: the anime's ID
        :return: dict or None
        :rtype: dict or NoneType
        """
        query_string = """\
            query ($id: Int) {
                Studio(id: $id) {
                    name
                }
            }
        """
        vars = {"id": item_id}
        r = requests.post(self.settings['apiurl'],
                          headers=self.settings['header'],
                          json={'query': query_string, 'variables': vars})
        jsd = r.text

        try:
            jsd = json.loads(jsd)
        except ValueError:
            return None
        else:
            return jsd

    def character(self, item_id):
        """
        The function to retrieve a character's details.

        :param int item_id: the anime's ID
        :return: dict or None
        :rtype: dict or NoneType
        """
        query_string = """\
            query ($id: Int) {
                Character (id: $id) {
                    name {
                        first
                        last
                        native
                    }
                    description
                    image {
                        large
                    }
                }
            }
        """
        vars = {"id": item_id}
        r = requests.post(self.settings['apiurl'],
                          headers=self.settings['header'],
                          json={'query': query_string, 'variables': vars})
        jsd = r.text

        try:
            jsd = json.loads(jsd)
        except ValueError:
            return None
        else:
            return jsd

    def review(self, item_id, html = True):
        """
        With the change to v2 of the api, reviews have their own IDs. This accepts the ID of the review.
        You can set html to False if you want the review body returned without html formatting.
        The API Default is true.

        :param item_id: the Id of the review
        :param html: do you want the body returned with html formatting?
        :return: json object
        :rtype: json object containing review information
        """
        query_string = """\
            query ($id: Int, $html: Boolean) {
                Review (id: $id) {
                    summary
                    body(asHtml: $html)
                    score
                    rating
                    ratingAmount
                    createdAt
                    updatedAt
                    private
                    media {
                        id
                    }
                    user {
                        id
                        name
                        avatar {
                            large
                        }
                    }
                }
            }
        """
        vars = {"id": item_id, "html": html}
        r = requests.post(self.settings['apiurl'],
                          headers=self.settings['header'],
                          json={'query': query_string, 'variables': vars})
        jsd = r.text

        try:
            jsd = json.loads(jsd)
        except ValueError:
            return None
        else:
            return jsd
