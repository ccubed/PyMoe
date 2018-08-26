import requests
import threading
import os


class Dump:
    def __init__(self):
        self.urls = {
            0: "http://anidb.net/api/anime-titles.dat.gz",
            1: "http://anidb.net/api/anime-titles.xml.gz"
        }

    def download(which, destination=None):
        """
        I realize that the download for the dumps is going to take awhile.
        Given that, I've decided to approach this using threads.
        When you call this method, it will launch a thread to download the data.
        By default, the dump is dropped into the current working directory.
        If the directory given doesn't exist, we'll try to make it.
        Don't use '..' in the path as this confuses makedirs.

        :param int which: 0 for dat (txt), 1 for xml
        :param str destination: a file path to save to, defaults to cwd
        """
        if destination:
            if not os.path.exists(destination):
                os.makedirs(destination)

        pthread = threading.Thread(
            target=save,
            args=(
                self.urls[which],
                os.path.join(destination, self.urls[which])
            )
        )
        pthread.start()
        return pthread


def save(url, destination):
    """
    This is just the thread target.
    It's actually responsible for downloading and saving.

    :param str url: which dump to download
    :param str destination: a file path to save to
    """
    r = requests.get(url, stream=True)

    with open(destination, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)
