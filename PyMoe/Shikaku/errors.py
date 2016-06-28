class ShikakuError(Exception):
    """
    Just to be clear on where they came from
    """
    pass

class NotFileBased(ShikakuError):
    """
    Raised when calling save and load on a backend that isn't file based. (So not json)
    """
    def __repr__(self):
        return "Can't save or load a backend that isn't file based."

class InvalidBackend(ShikakuError):
    """
    Raised when specifying an invalid backend.
    """
    def __init__(self, backend):
        self.message = backend

    def __repr__(self):
        return "{} isn't in the list of available backends.".format(self.message)
