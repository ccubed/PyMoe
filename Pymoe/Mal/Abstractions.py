from collections import namedtuple

class NT_EPISODES:
    """
    Abstraction for Episode data. Total is the total number of episodes. Current is the user's current episode number.
    """
    def __init__(self, current, total):
        self.current = current
        self.total = total

    def __repr__(self):
        return 'NT_EPISODES(current={}, total={})'.format(repr(self.current), repr(self.total))


class NT_SCORES:
    """
    Abstraction for score data. Average is the score as per all ratings as returned by searches. user is the user's score for this item.
    """
    def __init__(self, average, user):
        self.average = average
        self.user = user

    def __repr__(self):
        return 'NT_SCORES(average={}, user={})'.format(repr(self.average), repr(self.user))


class NT_STATUS:
    """
    Abstraction for status data. Series is the anime or manga status. user is the user's status for this thing.
    """
    def __init__(self, series, user):
        self.series = series
        self.user = user

    def __repr__(self):
        return 'NT_STATUS(series={}, user={})'.format(repr(self.series), repr(self.user))


class NT_DATES:
    """
    Abstraction for dates. Series is the date data for the anime or manga as a whole. User is the user's start and finish dates.
    """
    def __init__(self, series, user):
        self.series = NT_DATE_OBJ(series)
        self.user = NT_DATE_OBJ(user)

    def __repr__(self):
        return 'NT_DATES(series={}, user={})'.format(repr(self.series), repr(self.user))


class NT_DATE_OBJ:
    """
    Abstraction for the individual start and end dates since both the users and series have start/end tuples.
    """
    def __init__(self, dates):
        self.start = dates[0]
        self.end = dates[1]

    def __repr__(self):
        return 'NT_DATE_OBJ(start={}, end={})'.format(repr(self.start), repr(self.end))


class NT_STORAGE:
    """
    Storage type/value abstraction.
    """
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return 'NT_STORAGE(type={}, value={})'.format(repr(self.type), repr(self.value))

class NT_REWATCHED:
    """
    Rewatched/Rereading times/value abstraction.
    """
    def __init__(self, times, value):
        self.times = times
        self.value = value

    def __repr__(self):
        return 'NT_REWATCHED(times={}, value={})'.format(repr(self.times), repr(self.value))


class NT_FLAGS:
    """
    Abstraction for flag data such as discussion enabling and rewatching/rereading enabling.
    """
    def __init__(self, discussion, rewatching=None, rereading=None):
        self.discussion = discussion
        self.rewatching = rewatching
        self.rereading = rereading

    def __repr__(self):
        return 'NT_FLAGS(discussion={}, rewatching={}, rereading={})'.format(repr(self.discussion),
                                                                             repr(self.rewatching),
                                                                             repr(self.rereading))


#: Abstraction for anime methods.
NT_ANIME = namedtuple('NT_ANIME', ['search', 'add', 'update', 'delete'])


#: Abstraction for manga methods.
NT_MANGA = namedtuple('NT_MANGA', ['search', 'add', 'update', 'delete'])


#: Abstraction for User Anime and Manga data.
NT_TYPEDATA = namedtuple('NT_TYPEDATA', ['list', 'days'])

#: Abstraction for search instances for Anime
NT_SEARCH_ANIME = namedtuple("NT_SEARCH_ANIME", ['airing', 'finished', 'unaired', 'dropped', 'planned'])

#: Abstraction for search instances for Manga
NT_SEARCH_MANGA = namedtuple("NT_SEARCH_MANGA", ['publishing', 'finished', 'unpublished', 'dropped', 'planned'])

#: Abstraction for user Anime
NT_USER_ANIME = namedtuple("NT_USER_ANIME", ['watching', 'completed', 'held', 'dropped', 'planned'])

#: Abstraction for user Manga
NT_USER_MANGA = namedtuple("NT_USER_MANGA", ['reading', 'completed', 'held', 'dropped', 'planned'])


#: Status int to Name
STATUS_INTS = {
    'anime': {'1': 'Currently Airing', '2': 'Finished Airing', '3': 'Not Yet Aired', '4': 'Dropped', '6': 'Plan to Watch'},
    'manga': {'1': 'Publishing', '2': 'Finished', '3': 'Not Yet Published', '4': 'Dropped', '6': 'Plan to Read'},
    'user': {
        'anime': {'1': 'Currently Watching', '2': 'Completed', '3': 'On Hold', '4': 'Dropped', '6': 'Plan to Watch'},
        'manga': {'1': 'Currently Reading', '2': 'Completed', '3': 'On Hold', '4': 'Dropped', '6': 'Plan to Read'}
    }
}
