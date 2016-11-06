Errors
======

PyMoe defines several errors inside a superclassed MoeError so that you can always be clear where they come from and/or catch the superclass MoeError when you don't want to catch individual errors.

.. py:class:: MoeError

    Just the superclass of the Exceptions

.. py:class:: NoSSL

    Raised when we can't load the SSL library. Only relevant for VNDB.

.. py:class:: UserLoginFailed

    Raised when the server rejected our login credentials.

    .. py:attribute:: msg

        A string containing the message from the server. If one wasn't given, then it's a default failure message.

.. py:class:: GeneralLoginError

    Raised when we can't login for any reason other than credentials. Generally only for VNDB but can also be used for other services.

    .. py:attribute:: msg

        A string containing the message from the server. If one wasn't given, then it's a default failure message.

.. py:class:: ServerError

    If a server error is encountered during processing of some command, this error is raised.

    .. py:attribute:: msg

        The error message returned by the server.

    .. py:attribute:: code

        The error code returned by the server. This defaults to 500. It need not be an int. VNDB uses strings for instance.
