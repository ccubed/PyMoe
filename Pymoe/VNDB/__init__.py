from .connection import *

class VNDB:
    """
        Start up a vndb instance. This instance allows you to communicate with the VNDB d11 api. If you pass a username
        and password it will log you in as that user automatically. Since there can only be one user per connection,
        you will need to call this multiple times to log in as more than one user. However, this is possible.
        Simply create multiple instances. However, keep in mind that you can only ever have 10 connections per IP
        and 200 commands per 10 minutes per IP and 1 second of SQL time per minute per IP, so I doubt that multiple
        connections will be very fruitful.

        :param username: The username to log in as
        :param password: The password for that username
        :ivar VNDBConnection connection: The connection manager instance
    """
    def __init__(self, username=None, password=None):
        self.connection = VNDBConnection(username, password)
