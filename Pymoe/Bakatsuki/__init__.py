import requests
import re
from bs4 import BeautifulSoup as soup
from ..errors import *

class Bakatsuki:
    """
        :ivar str api: API Url for Bakatsuki
        :ivar dict header: Predefined Headers for our calls
        :ivar str active_id: Category ID for active projects
        :ivar SRE_Pattern chapter_regex: Helps parsing chapters
        :ivar SRE_Pattern separate_regex: Pulls the # out of the chapters/sections
    """

    def __init__(self):
        """
        Initialize a new Bakatsuki API Interface
        """
        self.api = "https://www.baka-tsuki.org/project/api.php"
        self.header = {'User-Agent': 'Pymoe (git.vertinext.com/ccubed/Pymoe)'}
        self.active_id = "56132"
        self.chapter_regex = re.compile("volume|chapter")
        self.separate_regex = re.compile("(volume|chapter) (?P<chapter>[0-9]{1,2})")

    def active(self):
        """
        Get a list of active projects.

        :return list: A list of tuples containing a title and pageid in that order.
        """
        projects = []
        r = requests.get(self.api,
                         params={'action': 'query', 'list': 'categorymembers', 'cmpageid': self.active_id,
                                 'cmtype': 'page', 'cmlimit': '500', 'format': 'json'},
                         headers=self.header)
        if r.status_code == 200:
            jsd = r.json()
            projects.append([(x['title'], x['pageid']) for x in jsd['query']['categorymembers']])
            if 'query-continue' in jsd:
                while True:
                    r = requests.get(self.api,
                                     params={'action': 'query', 'list': 'categorymembers',
                                             'cmpageid': self.active_id, 'cmtype': 'page', 'cmlimit': '500',
                                             'cmcontinue': jsd['query-continue']['categorymembers']['cmcontinue'],
                                             'format': 'json'},
                                     headers=self.header)
                    if r.status_code == 200:
                        jsd = r.json()
                        projects.append([(x['title'], x['pageid']) for x in jsd['query']['categorymembers']])
                        if 'query-continue' not in jsd:
                            break
                    else:
                        break
        return projects

    def light_novels(self, language="English"):
        """
        Get a list of light novels under a certain language.

        :param str language: Defaults to English. Replace with whatever language you want to query.
        :return list: A list of tuples containing a title and pageid element in that order.
        """
        projects = []
        r = requests.get(self.api,
                         params={'action': 'query', 'list': 'categorymembers',
                                 'cmtitle': 'Category:Light_novel_({})'.format(language.replace(" ", "_")),
                                 'cmtype': 'page', 'cmlimit': '500', 'format': 'json'},
                         headers=self.header)
        if r.status_code == 200:
            jsd = r.json()
            projects.append([(x['title'], x['pageid']) for x in jsd['query']['categorymembers']])
            if 'query-continue' in jsd:
                while True:
                    r = requests.get(self.api,
                                     params={'action': 'query', 'list': 'categorymembers',
                                             'cmtitle': 'Category:Light_novel_({})'.format(language.replace(" ", "_")),
                                             'cmtype': 'page', 'cmlimit': '500',
                                             'cmcontinue': jsd['query-continue']['categorymembers']['cmcontinue'],
                                             'format': 'json'},
                                     headers=self.header)
                    if r.status_code == 200:
                        jsd = r.json()
                        projects.append([(x['title'], x['pageid']) for x in jsd['query']['categorymembers']])
                        if 'query-continue' not in jsd:
                            break
                    else:
                        break
        return projects

    def teaser(self, language="English"):
        """
        Get a list of teaser projects under a certain language.

        :param str language: Defaults to English. Replace with whatever language you want to query.
        :return list: A list of tuples containing a title and pageid element in that order.
        """
        projects = []
        r = requests.get(self.api,
                         params={'action': 'query', 'list': 'categorymembers',
                                 'cmtitle': 'Category:Teaser_({})'.format(language.replace(" ", "_")),
                                 'cmtype': 'page', 'cmlimit': '500', 'format': 'json'},
                         headers=self.header)
        if r.status_code == 200:
            jsd = r.json()
            projects.append([(x['title'], x['pageid']) for x in jsd['query']['categorymembers']])
            if 'query-continue' in jsd:
                while True:
                    r = requests.get(self.api,
                                     params={'action': 'query', 'list': 'categorymembers',
                                             'cmtitle': 'Category:Teaser_({})'.format(language.replace(" ", "_")),
                                             'cmtype': 'page', 'cmlimit': '500',
                                             'cmcontinue': jsd['query-continue']['categorymembers']['cmcontinue'],
                                             'format': 'json'},
                                     headers=self.header)
                    if r.status_code == 200:
                        jsd = r.json()
                        projects.append([(x['title'], x['pageid']) for x in jsd['query']['categorymembers']])
                        if 'query-continue' not in jsd:
                            break
                    else:
                        break
        return projects

    def web_novels(self, language="English"):
        """
        Get a list of web novels under a certain language.

        :param str language: Defaults to English. Replace with whatever language you want to query.
        :return list: A list of tuples containing a title and pageid element in that order.
        """
        projects = []
        r = requests.get(self.api,
                         params={'action': 'query', 'list': 'categorymembers',
                                 'cmtitle': 'Category:Web_novel_({})'.format(language.replace(" ", "_")),
                                 'cmtype': 'page', 'cmlimit': '500', 'format': 'json'},
                         headers=self.header)
        if r.status_code == 200:
            jsd = r.json()
            projects.append([(x['title'], x['pageid']) for x in jsd['query']['categorymembers']])
            if 'query-continue' in jsd:
                while True:
                    r = requests.get(self.api,
                                     params={'action': 'query', 'list': 'categorymembers',
                                             'cmtitle': 'Category:Web_novel_({})'.format(language.replace(" ", "_")),
                                             'cmtype': 'page', 'cmlimit': '500',
                                             'cmcontinue': jsd['query-continue']['categorymembers']['cmcontinue'],
                                             'format': 'json'},
                                     headers=self.header)
                    if r.status_code == 200:
                        jsd = r.json()
                        projects.append([(x['title'], x['pageid']) for x in jsd['query']['categorymembers']])
                        if 'query-continue' not in jsd:
                            break
                    else:
                        break
        return projects

    def chapters(self, title):
        """
        Get a list of chapters for a visual novel. Keep in mind, this can be slow. I've certainly tried to make it as fast as possible, but it's still pulling text out of a webpage.

        :param str title: The title of the novel you want chapters from
        :return dict: A dictionary with a sorted and data element. Sorted contains the data dictionary's keys in numeric sort from 0 or 1 to whatever. Data isn't necessarily sorted but contains a list where index 0 is the link and index 1 is the title of the chapter.
        """
        r = requests.get("https://www.baka-tsuki.org/project/index.php?title={}".format(title.replace(" ", "_")),
                         headers=self.header)
        if r.status_code != 200:
            raise requests.HTTPError("Not Found")
        else:
            parsed = soup(r.text, 'lxml')
            dd = parsed.find_all("a")
            volumes = []
            for link in dd:
                if 'class' in link.attrs:
                    if 'image' in link.get('class'):
                        continue
                if 'href' in link.attrs:
                    if re.search(self.chapter_regex, link.get('href')) is not None and not link.get('href').startswith('#'):
                        volumes.append(link)
            seplist = {}
            for item in volumes:
                result = re.search(self.separate_regex, item.get('title').lower())
                if result.group('chapter').lstrip('0') in seplist:
                    seplist[result.group('chapter').lstrip('0')].append([item.get('href'), item.get('title')])
                else:
                    seplist[result.group('chapter').lstrip('0')] = [[item.get('href'), item.get('title')]]
            del volumes
            return {'sorted': sorted([int(x) for x in seplist.keys()]), 'data': seplist}

    def cover(self, pageid):
        """
        Get a cover image given a page id.

        :param str pageid: The pageid for the light novel you want a cover image for
        :return str: the image url
        """
        r = requests.get(self.api,
                         params={'action': 'query', 'prop': 'pageimages', 'pageids': pageid, 'format': 'json'},
                         headers=self.header)
        jsd = r.json()
        image = "File:" + jsd['query']['pages'][pageid]['pageimage']
        r = requests.get(self.api,
                         params={'action': 'query', 'prop': 'imageinfo', 'iiprop': 'url', 'titles': image,
                                 'format': 'json'},
                         headers=self.header)
        jsd = r.json()
        return jsd['query']['pages'][list(jsd.keys)[0]]['imageinfo']['url']

    def search(self, title):
        """
        Search content by title. Not implemented Yet!

        :param str title: The title of the content you want to find.
        :return: A list of tuples containing the titles and pageids of the results in that order.
        """
        pass
