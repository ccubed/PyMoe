from collections import namedtuple

#: Abstraction for Episode data. Total is the total number of episodes. Current is the user's current episode number.
NT_EPISODES = namedtuple('NT_EPISODES', ['total', 'current'])

#: Abstraction for score data. Average is the score as per all ratings as returned by searches. user is the user's score for this item.
NT_SCORES = namedtuple('NT_SCORES', ['average', 'user'])

#: Abstraction for status data. Series is the anime or manga status. user is the user's status for this thing.
NT_STATUS = namedtuple('NT_STATUS', ['series', 'user'])

#: Abstraction for dates. Series is the date data for the anime or manga as a whole. User is the user's start and finish dates.
NT_DATES = namedtuple('NT_DATES', ['series', 'user'])

#: Abstraction for the individual start and end dates since both the users and series have start/end tuples.
NT_DATE_OBJ = namedtuple('NT_DATE_OBJ', ['start', 'end'])

#: Storage type/value abstraction.
NT_STORAGE = namedtuple('NT_STORAGE', ['type', 'value'])

#: Rewatched/Rereading times/value abstraction.
NT_REWATCHED = namedtuple('NT_REWATCHED', ['times', 'value'])

#: Abstraction for flag data such as discussion enabling and rewatching/rereading enabling.
NT_FLAGS = namedtuple('NT_FLAGS', ['discussion', 'rewatching', 'rereading'])

#: Abstraction for anime methods.
NT_ANIME = namedtuple('NT_ANIME', ['search', 'add', 'update', 'delete'])

#: Abstraction for manga methods.
NT_MANGA = namedtuple('NT_MANGA', ['search', 'add', 'update', 'delete'])

#: Abstraction for User Anime and Manga data.
NT_TYPEDATA = namedtuple('NT_TYPEDATA', ['list', 'stats'])

#: Abstraction for user anime and manga stats.
NT_STATS = namedtuple('NT_TYPESTATS', ['completed', 'onhold', 'dropped', 'planned', 'current', 'days'])
