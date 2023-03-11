import requests
import ujson
from ...errors import serverError, serializationFailed

settings = {
    'apiurl': "https://www.baka-tsuki.org/project/api.php",
    'header': {
        'User-Agent': 'Pymoe (github.com/ccubed/Pymoe)'
    }
}

def lightNovels(language: str = "English"):
    """
        Get a list of light novels under a certain language.

        :param str language: Defaults to English. Replace with whatever language you want to query. You can check their site for the language attributes.
        :return list: A list of tuples containing a title and pageid element in that order.
    """
    projects = []

    r = requests.get(
        settings['apiurl'],
        params = {
            'action': 'query',
            'list': 'categorymembers',
            'cmtitle': 'Category:Light_novel_({})'.format(language.replace(" ", "_")),
            'cmtype': 'page',
            'cmlimit': '500',
            'format': 'json'
        }
    )
    
    if r.status_code != 200:
        raise serverError(r.text, r.status_code)
    else:
        try:
            jsd = ujson.loads(r.text)
        except ValueError:
            raise serializationFailed(r.text, r.status_code)
        else:
            projects.append(
                [(x['title'], x['pageid']) for x in jsd['query']['categorymembers']]
            )

            if 'query-continue' in jsd:
                while True:
                    r = requests.get(
                        settings['apiurl'],
                        params = {
                            'action': 'query',
                            'list': 'categorymembers',
                            'cmtitle': 'Category:Light_novel_({})'.format(language.replace(" ", "_")),
                            'cmtype': 'page', 
                            'cmlimit': '500',
                            'cmcontinue': jsd['query-continue']['categorymembers']['cmcontinue'],
                            'format': 'json'
                        },
                        headers = settings['header']
                    )

                    if r.status_code != 200:
                        break
                    else:
                        try:
                            jsd = ujson.loads(r.text)
                        except ValueError:
                            break
                        else:
                            projects.append(
                                [(x['title'], x['pageid']) for x in jsd['query']['categorymembers']]
                            )
                            if 'query-continue' not in jsd:
                                break
            
            return projects[0]

def teasers(language: str = "English"):
    """
        Get a list of teaser projects under a certain language.

        :param str language: Defaults to English. Replace with whatever language you want to query.
        :return list: A list of tuples containing a title and pageid element in that order.
    """
    projects = []

    r = requests.get(
        settings['apiurl'],
        params = {
            'action': 'query',
            'list': 'categorymembers',
            'cmtitle': 'Category:Teaser_({})'.format(language.replace(" ", "_")),
            'cmtype': 'page',
            'cmlimit': '500',
            'format': 'json'
        }
    )
    
    if r.status_code != 200:
        raise serverError(r.text, r.status_code)
    else:
        try:
            jsd = ujson.loads(r.text)
        except ValueError:
            raise serializationFailed(r.text, r.status_code)
        else:
            projects.append(
                [(x['title'], x['pageid']) for x in jsd['query']['categorymembers']]
            )

            if 'query-continue' in jsd:
                while True:
                    r = requests.get(
                        settings['apiurl'],
                        params = {
                            'action': 'query',
                            'list': 'categorymembers',
                            'cmtitle': 'Category:Teaser_({})'.format(language.replace(" ", "_")),
                            'cmtype': 'page', 
                            'cmlimit': '500',
                            'cmcontinue': jsd['query-continue']['categorymembers']['cmcontinue'],
                            'format': 'json'
                        },
                        headers = settings['header']
                    )

                    if r.status_code != 200:
                        break
                    else:
                        try:
                            jsd = ujson.loads(r.text)
                        except ValueError:
                            break
                        else:
                            projects.append(
                                [(x['title'], x['pageid']) for x in jsd['query']['categorymembers']]
                            )
                            if 'query-continue' not in jsd:
                                break
            
            return projects[0]

def webNovels(language: str = "English"):
    """
        Get a list of web novels under a certain language.

        :param str language: Defaults to English. Replace with whatever language you want to query.
        :return list: A list of tuples containing a title and pageid element in that order.
    """
    projects = []

    r = requests.get(
        settings['apiurl'],
        params = {
            'action': 'query',
            'list': 'categorymembers',
            'cmtitle': 'Category:Web_novel_({})'.format(language.replace(" ", "_")),
            'cmtype': 'page',
            'cmlimit': '500',
            'format': 'json'
        }
    )
    
    if r.status_code != 200:
        raise serverError(r.text, r.status_code)
    else:
        try:
            jsd = ujson.loads(r.text)
        except ValueError:
            raise serializationFailed(r.text, r.status_code)
        else:
            projects.append(
                [(x['title'], x['pageid']) for x in jsd['query']['categorymembers']]
            )

            if 'query-continue' in jsd:
                while True:
                    r = requests.get(
                        settings['apiurl'],
                        params = {
                            'action': 'query',
                            'list': 'categorymembers',
                            'cmtitle': 'Category:Web_novel_({})'.format(language.replace(" ", "_")),
                            'cmtype': 'page', 
                            'cmlimit': '500',
                            'cmcontinue': jsd['query-continue']['categorymembers']['cmcontinue'],
                            'format': 'json'
                        },
                        headers = settings['header']
                    )

                    if r.status_code != 200:
                        break
                    else:
                        try:
                            jsd = ujson.loads(r.text)
                        except ValueError:
                            break
                        else:
                            projects.append(
                                [(x['title'], x['pageid']) for x in jsd['query']['categorymembers']]
                            )
                            if 'query-continue' not in jsd:
                                break
            
            return projects[0]