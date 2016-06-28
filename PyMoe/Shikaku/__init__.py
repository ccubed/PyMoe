import importlib
import os.path
import inspect
from .errors import *


class Shikaku:
    def __init__(self, root="PyMoe", backend="json"):
        """
        Initialize a new Shikaku credential manager. By default, Shikaku uses a blank Json interface.
        From there you can load data into it or switch it to another backend.

        :param root: If using postgresql, sqlite, mysql or mongo then this is the name of the DB.
        """
        if backend not in ['json', 'mongo', 'mysql', 'postgresql', 'redis', 'sqlite']:
            raise InvalidBackend
        self.root = root
        self.backend = Backend(backend, importlib.import_module('Backends.{}'.format(backend)))

    def save(self, path=None):
        if self.backend.name != "json":
            return NotFileBased
        if path:
            self.backend.instance.save(path)
        else:
            self.backend.instance.save(os.path.expanduser('~/.config/PyMoe/credentials.json'))

    def load(self, path=None):
        if self.backend.name != "json":
            return NotFileBased
        if path:
            self.backend.instance.load(path)
        else:
            self.backend.instance.load(os.path.expanduser('~/.config/PyMoe/credentials.json'))

    def set_backend(self, backend):
        if backend.name == 'json':
            self.save(os.path.expanduser('~/.config/PyMoe/credentials.bak'))
        if backend in ['json', 'mongo', 'mysql', 'postgresql', 'redis', 'sqlite']:
            del self.backend
            self.backend = Backend(backend, importlib.import_module('Backends.{}'.format(backend)))
        else:
            return InvalidBackend

    def set(self, domain, key, data):
        pass

    def delete(self, domain, key):
        pass

    def get(self, domain, key):
        pass


class Backend:
    def __init__(self, name, instance):
        self.name = name
        self.instance = inspect.getmembers(instance, inspect.isclass)[0][1]()