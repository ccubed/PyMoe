from collections import namedtuple

NT_EPISODES = namedtuple('episodes', ['total', 'current'])
NT_SCORES = namedtuple('scores', ['average', 'user'])
NT_STATUS = namedtuple('status', ['anime', 'user'])
NT_DATES = namedtuple('dates', ['anime', 'user'])
NT_DATE_OBJ = namedtuple('date_data', ['start', 'end'])
NT_STORAGE = namedtuple('storage', ['type', 'value'])
NT_REWATCHED = namedtuple('rewatched', ['times', 'value'])
NT_FLAGS = namedtuple('flags', ['discussion', 'rewatching', 'rereading'])