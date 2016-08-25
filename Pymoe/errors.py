class MoeError(Exception):
    """
    Just making it more clear where the error comes from
    """
    pass


class NoSSL(MoeError):
    """
    Raised when we can't import SSL. Necessary for TLS and SSL Socket Wraps.
    """
    def __repr__(self):
        return "No SSL Library available. Please install OpenSSL or some alternative."

class UserLoginFailed(MoeError):
    """
    Raised when user details were not authenticated by the endpoint for the API.
    If available, a message that was provided from the API is given.
    Otherwise, it's just a login failed message.
    """
    def __init__(self, msg):
        self.message = msg

    def __repr__(self):
        return "We attempted to login using those details but got an error.\nError: {}".format(self.message)

class GeneralLoginError(MoeError):
    """
    Raised when an API refuses to allow us to login for some reason other than user credentials. Mostly for VNDB.
    """
    def __init__(self, msg):
        self.message = msg

    def __repr__(self):
        return "We attempted to login but the server responded with: {}".format(self.message)

class ServerError(MoeError):
    """
    Raised when we encounter an error retrieving information from the server.
    """
    def __init__(self, message=None, code=500):
        self.msg = message
        self.code = code

    def __repr__(self):
        if self.msg:
            return "Server Error encounted.\nCode: {}\nMessage: {}".format(self.code, self.msg)
        else:
            return "Encountered a server error attempting to access information."
