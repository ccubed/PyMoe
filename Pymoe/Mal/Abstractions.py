from collections import namedtuple

class NT_EPISODES:
    """
    Abstraction for Episode data. Total is the total number of episodes. Current is the user's current episode number.
    """
    def __init__(self, current, total):
        self.current = current
        self.total = total


class NT_SCORES:
    """
    Abstraction for score data. Average is the score as per all ratings as returned by searches. user is the user's score for this item.
    """
    def __init__(self, average, user):
        self.average = average
        self.user = user


class NT_STATUS:
    """
    Abstraction for status data. Series is the anime or manga status. user is the user's status for this thing.
    """
    def __init__(self, series, user):
        self.series = series
        self.user = user


class NT_DATES:
    """
    Abstraction for dates. Series is the date data for the anime or manga as a whole. User is the user's start and finish dates.
    """
    def __init__(self, series, user):
        self.series = NT_DATE_OBJ(series)
        self.user = NT_DATE_OBJ(user)


class NT_DATE_OBJ:
    """
    Abstraction for the individual start and end dates since both the users and series have start/end tuples.
    """
    def __init__(self, dates):
        self.start = dates[0]
        self.end = dates[1]


class NT_STORAGE:
    """
    Storage type/value abstraction.
    """
    def __init__(self, type, value):
        self.type = type
        self.value = value


class NT_REWATCHED:
    """
    Rewatched/Rereading times/value abstraction.
    """
    def __init__(self, times, value):
        self.times = times
        self.value = value


class NT_FLAGS:
    """
    Abstraction for flag data such as discussion enabling and rewatching/rereading enabling.
    """
    def __init__(self, discussion, rewatching=None, rereading=None):
        self.discussion = discussion
        self.rewatching = rewatching
        self.rereading = rereading


#: Abstraction for anime methods.
NT_ANIME = namedtuple('NT_ANIME', ['search', 'add', 'update', 'delete'])


#: Abstraction for manga methods.
NT_MANGA = namedtuple('NT_MANGA', ['search', 'add', 'update', 'delete'])


#: Abstraction for User Anime and Manga data.
NT_TYPEDATA = namedtuple('NT_TYPEDATA', ['list', 'stats'])


#: Abstraction for user anime and manga stats.
NT_STATS = namedtuple('NT_TYPESTATS', ['completed', 'onhold', 'dropped', 'planned', 'current', 'days'])


#: Status int to Name
STATUS_INTS_ANIME = ['Currently Airing', 'Finished Airing', 'Not Yet Aired', 'Dropped', 'Plan to Watch']


#: Status int to Name
STATUS_INTS_MANGA = ['Publishing', 'Finished', 'Not Yet Published', 'Dropped', 'Plan to Read']