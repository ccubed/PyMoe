class moeError(Exception):
    """
    Just making it more clear where the error comes from
    """

    pass


class serverError(moeError):
    """
    Raised when we encounter an error retrieving information from the server.
    """

    def __init__(self, message: str = None, code: int = 500):
        self.message = message
        self.code = code

    def __repr__(self):
        if self.msg:
            return "Server Error encounted.\nCode: {}\nMessage: {}".format(
                self.code, self.message
            )
        else:
            return "Encountered a server error attempting to access information. \nCode: {}".format(
                self.code
            )


class methodNotSupported(moeError):
    """
    Raised when an operation is requested on an Interface that does not support it.
    """

    def __init__(self, operation: str, interface: str):
        self.operation = operation
        self.interface = interface

    def __repr__(self):
        return "Operation {} not supported on Interface {}.".format(
            self.operation, self.interface
        )


class serializationFailed(moeError):
    """
    Raised when ujson fails to load the data sent by the server.
    Originally this raised a ServerError because I wanted to maintain the response from the server.
    However, ServerError doesn't really explain where the erorr happened.
    This does a better job of saving the response and also more clearly indicating the source of the error.
    """

    def __init__(self, message: str = None, code: int = 500):
        self.message = message
        self.code = code

    def __repr__(self):
        return "Ujson failed to parse response from server.\nStatus Code: {}\nServer Response:\n{}".format(
            self.code, self.message
        )
