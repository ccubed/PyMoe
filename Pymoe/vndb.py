from .errors import *
import socket
import re
import ujson

try:
    import ssl
except ImportError:
    raise NoSSL


class Vndb:
    def __init__(self, username=None, password=None):
        """
        Start up a vndb instance. This instance allows you to communicate with the VNDB d11 api. If you pass a username
        and password it will log you in as that user automatically. Since there can only be one user per connection,
        you will need to call this multiple times to log in as more than one user. However, this is possible.
        Simply create multiple instances. However, keep in mind that you can only ever have 10 connections per IP
        and 200 commands per 10 minutes per IP and 1 second of SQL time per minute per IP, so I doubt that multiple
        connections will be very fruitful.

        :param username: The username to log in as
        :param password: The password for that username
        """
        self.clientvars = {'protocol': 1, 'clientver': 0.1, 'client': 'Pymoe'}
        self.user = False
        self.data_buffer = bytes(1024)
        self.sslcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        self.sslcontext.verify_mode = ssl.CERT_REQUIRED
        self.sslcontext.check_hostname = True
        self.sslcontext.load_default_certs()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sslwrap = self.sslcontext.wrap_socket(self.socket, server_hostname='api.vndb.org')
        self.sslwrap.connect(('api.vndb.org', 19535))
        self.helperpat = re.compile('[=|!=|~|>|>=|<=|<]')
        self.login(username, password)

    def close(self):
        """
        Close the socket connection.

        :return: None
        """
        self.sslwrap.close()

    def login(self, username, password):
        """
        This handles login logic instead of stuffing all that in the __init__.

        :param username: The username to log in as or None
        :param password: The password for that user or None
        :return: None but can raise an error
        """
        finvars = self.clientvars
        if username and password:
            finvars['username'] = username
            finvars['password'] = password
            self.user = True
        ret = self.send_command('login', ujson.dumps(finvars))
        if not isinstance(ret, str):  # should just be 'Ok'
            if self.user:
                self.user = False
                raise UserLoginFailed(ret['msg'])
            else:
                raise GeneralLoginError(ret['msg'])

    def send_command(self, command, args):
        """
        Send a command to VNDB and then get the result.

        :param command: What command are we sending
        :param args: What are the json args for this command
        :return: Servers Response
        """
        if isinstance(args, str):
            final_command = command + ' ' + args + '\x04'
        else:
            # We just let ujson propogate the error here if it can't parse the arguments
            final_command = command + ' ' + ujson.dumps(args) + '\x04'
        self.sslwrap.sendall(final_command.encode('utf-8'))
        return self._recv_data()

    def _recv_data(self):
        """
        Receieves data until we reach the \x04 and then returns it.

        :return: The data received
        """
        temp = ""
        while True:
            self.data_buffer = self.sslwrap.recv(1024)
            if '\x04' in self.data_buffer.decode('utf-8', 'ignore'):
                temp += self.data_buffer.decode('utf-8', 'ignore')
                break
            else:
                temp += self.data_buffer.decode('utf-8', 'ignore')
                self.data_buffer = bytes(1024)
        temp = temp.replace('\x04', '')
        if 'Ok' in temp:  # Because login
            return temp
        else:
            return ujson.loads(temp.split(' ', 1)[1])

