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
    def __init__(self, message : str):
        self.message = message

    def __repr__(self):
        return "We attempted to login using those details but got an error.\nError: {}".format(self.message)

class GeneralLoginError(MoeError):
    """
    Raised when an API refuses to allow us to login for some reason other than user credentials. Mostly for VNDB.
    """
    def __init__(self, message : str):
        self.message = message

    def __repr__(self):
        return "We attempted to login but the server responded with: {}".format(self.message)

class ServerError(MoeError):
    """
    Raised when we encounter an error retrieving information from the server.
    """
    def __init__(self, message : str = None, code : int = 500):
        self.message = message
        self.code = code

    def __repr__(self):
        if self.msg:
            return "Server Error encounted.\nCode: {}\nMessage: {}".format(self.code, self.message)
        else:
            return "Encountered a server error attempting to access information. \nCode: {}".format(self.code)

class MethodNotSupported(MoeError):
    """
        Raised when an operation is requested on an Interface that does not support it.
    """
    def __init__(self, operation : str, interface : str):
        self.operation = operation
        self.interface = interface

    def __repr__(self):
        return "Operation {} not supported on Interface {}.".format(self.operation, self.interface)

class SerializationFailed(MoeError):
    """
        Raised when ujson fails to load the data sent by the server.
        Originally this raised a ServerError because I wanted to maintain the response from the server.
        However, ServerError doesn't really explain where the erorr happened.
        This does a better job of saving the response and also more clearly indicating the source of the error.
    """
    def __init__(self, message : str = None, code : int = 500):
        self.message = message
        self.code = code

    def __repr__(self):
        return "Ujson failed to parse response from server.\nStatus Code: {}\nServer Response:\n{}".format(self.code, self.message)