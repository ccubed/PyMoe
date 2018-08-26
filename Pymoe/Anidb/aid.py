import requests
import xml.etree.ElementTree as ET


class Aid:
    def __init__(self):
        pass

    def search(term, lang=None):
        """
        As a convenient alternative to downloading and parsing a dump,
        This function will instead query the AID search provided by Eloyard.
        This is the same information available at http://anisearch.outrance.pl/.

        :param str term: Search Term
        :param list lang: A list of language codes which determines what titles are returned
        """
        r = requests.get(
            "http://anisearch.outrance.pl/index.php",
            params={
                "task": "search",
                "query": term,
                "langs": "ja,x-jat,en" if lang is None else ','.join(lang)
            }
        )

        if r.status_code != 200:
            raise ServerError

        tree = ET.fromstring(r.text)
        root = tree.getroot()

        for item in root.iter("anime"):

            # Parse XML http://wiki.anidb.net/w/User:Eloyard/anititles_dump
            results[aid]={}
            for title in item.iter('title'):
                if title.attrib['type'] in ['official', 'main']:
                    results[aid][title.attrib['xml:lang']] = title.text
        
        return results
