from .Abstractions import NT_DATE_OBJ, NT_DATES, NT_EPISODES, NT_FLAGS, NT_REWATCHED, NT_SCORES, NT_STATUS, NT_STORAGE

class Anime:
    """
    An encapsulated Mal Anime Object for updates and adds.
    These can be created by the programmer or by the library, such as with searches or pulling user data.
    The XML data for updates, adds and other requests are gathered from the following attributes:
    episodes.current -> episode
    status.user -> status
    scores.user -> score
    rewatched.times -> times_rewatched
    rewatched.value -> rewatch_value
    storage.type -> storage_type
    storage.value -> storage_value
    dates.user.start -> date_start
    dates.user.end -> date_finish
    priority -> priority
    flags.discussion -> boolean to indicate whether it's enabled or disabled
    flags.rewatching -> boolean to indicate whether it's enabled or disabled
    comments -> comments
    fansub_group -> fansub_group
    tags -> tags
    """

    def __init__(self, aid, **kwargs):
        """
        This creates an Anime Object. At least the ID is required. All other args are optional.
        Any keyword args not specified will not be included in the XML in subsequent add/update requests.

        :param str aid: The Anime ID.
        :param int episode: Set the user's current episode.
        :param int score: Set the user's score.
        :param int status: Set the user's status for this anime. 1/watching,2/completed,3/onhold,4/dropped,6/plantowatch.
        :param str date_start: Set the date the user started this anime. Format should be MM-DD-YYYY.
        :param str date_finish: Set the date the user finished this anime. Format should be MM-DD-YYYY.
        :param int storage_type: Set the storage_type for this anime. 1/hard drive,2/dvdcd,3/none,4/retail dvd,5/vhs,6/external hd,7/nas,8/bluray.
        :param int storage_value: Set the storage_value for this anime. if type is 1,6 or 7 this is drive space (gb). 2,4,5 and 8 are # of discs/cds/whatever. this doesn't apply to 3.
        :param int rewatched: Set the number of times this anime has been rewatched.
        :param int rewatch_value: Set the rewatch value. 1 is very low, 3 is medium, 5 is very high. Goes in order.
        :param bool discussion: Discussion is on for this anime?
        :param bool rewatching: Currently rewatching this anime?
        :param int priority: 1-3, priority, low - high.
        :param str comments: Comments for this anime.
        :param list tags: List of str for tags.
        :param str fansub_group: Name of fansub group for this anime if any.
        """
        self.id = aid
        self.title = kwargs.get("title") or None
        self.synonyms = kwargs.get("synonyms") or None
        self.episodes = NT_EPISODES(total=kwargs.get('episodes'), current=kwargs.get('episode'))
        self.scores = NT_SCORES(average=kwargs.get('average'), user=kwargs.get('score'))
        self.type = kwargs.get('type')
        self.status = NT_STATUS(anime=kwargs.get('status_anime'), user=kwargs.get('status'))
        self.dates = NT_DATES(anime=NT_DATE_OBJ(start=kwargs.get('anime_start'), end=kwargs.get('anime_end')),
                               user=NT_DATE_OBJ(start=kwargs.get('date_start'), end=kwargs.get('date_finish')))
        self.synopsis = kwargs.get('synopsis')
        self.image = kwargs.get('image')
        self.storage = NT_STORAGE(type=kwargs.get('storage_type'), value=kwargs.get('storage_value'))
        self.rewatched = NT_REWATCHED(times=kwargs.get('rewatched'), value=kwargs.get('rewatch_value'))
        self.flags = NT_FLAGS(discussion=kwargs.get('discussion'), rewatching=kwargs.get('rewatching'))
        self.priority = kwargs.get('priority')
        self.comments = kwargs.get('comments')
        self.tags = kwargs.get('tags')
        self.fansub_group = kwargs.get('fansub_group')



class Manga:
    """
    An encapsulated Mal Manga Object for updates and adds.
    These can be created by the programmer or by the library, such as with searches or pulling user data.
    The XML data for updates, adds and other requests are gathered from the following attributes:
    chapters.current -> chapter
    volumes.current -> volume
    status.user -> status
    scores.user -> score
    reread.times -> times_reread
    reread.value -> rewatch_value
    storage.type -> storage_type
    storage.value -> storage_value
    dates.user.start -> date_start
    dates.user.end -> date_finish
    priority -> priority
    flags.discussion -> boolean to indicate whether it's enabled or disabled
    flags.rereading -> boolean to indicate whether it's enabled or disabled
    comments -> comments
    scan_group -> scan_group
    tags -> tags
    """

    def __init__(self, mid, **kwargs):
        """
        This creates a Manga Object. At least the ID is required. All other args are optional.
        Any keyword args not specified will not be included in the XML in subsequent add/update requests.

        :param str mid: The Manga ID.
        :param int chapter: Set the user's current chapter
        :param int volume: set the user's current volume
        :param int score: Set the user's score.
        :param int status: Set the user's status for this manga. 1/watching,2/completed,3/onhold,4/dropped,6/plantowatch.
        :param str date_start: Set the date the user started this manga. Format should be MM-DD-YYYY.
        :param str date_finish: Set the date the user finished this manga. Format should be MM-DD-YYYY.
        :param int storage_type: Set the storage_type for this manga. 1/hard drive,2/dvdcd,3/none,4/retail dvd,5/vhs,6/external hd,7/nas,8/bluray.
        :param int storage_value: Set the storage_value for this manga. if type is 1,6 or 7 this is drive space (gb). 2,4,5 and 8 are # of discs/cds/whatever. this doesn't apply to 3.
        :param int reread: Set the number of times this manga has been reread.
        :param int reread_value: Set the reread value. 1 is very low, 3 is medium, 5 is very high. Goes in order.
        :param bool discussion: Discussion is on for this manga?
        :param bool rereading: Currently rereading this manga?
        :param int priority: 1-3, priority, low - high.
        :param str comments: Comments for this manga.
        :param list tags: List of str for tags.
        :param str scan_group: Name of scanlation group for this manga if any.
        """
        self.id = mid
        self.title = kwargs.get("title") or None
        self.synonyms = kwargs.get("synonyms") or None
        self.chapters = NT_EPISODES(total=kwargs.get('chapters'), current=kwargs.get('chapter'))
        self.scores = NT_SCORES(average=kwargs.get('average'), user=kwargs.get('score'))
        self.type = kwargs.get('type')
        self.status = NT_STATUS(anime=kwargs.get('status_manga'), user=kwargs.get('status'))
        self.dates = NT_DATES(anime=NT_DATE_OBJ(start=kwargs.get('manga_start'), end=kwargs.get('manga_end')),
                              user=NT_DATE_OBJ(start=kwargs.get('date_start'), end=kwargs.get('date_finish')))
        self.synopsis = kwargs.get('synopsis')
        self.image = kwargs.get('image')
        self.storage = NT_STORAGE(type=kwargs.get('storage_type'), value=kwargs.get('storage_value'))
        self.reread = NT_REWATCHED(times=kwargs.get('reread'), value=kwargs.get('reread_value'))
        self.flags = NT_FLAGS(discussion=kwargs.get('discussion'), rereading=kwargs.get('rereading'))
        self.priority = kwargs.get('priority')
        self.comments = kwargs.get('comments')
        self.tags = kwargs.get('tags')
        self.scan_group = kwargs.get('scan_group')
