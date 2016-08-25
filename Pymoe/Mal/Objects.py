import xml.etree.ElementTree as ET
from .Abstractions import NT_DATE_OBJ, NT_DATES, NT_EPISODES, NT_FLAGS, NT_REWATCHED, NT_SCORES, NT_STATUS, NT_STORAGE, NT_TYPEDATA, NT_STATS


class Anime:
    """
    An encapsulated Mal Anime Object for updates and adds.\n
    These can be created by the programmer or by the library, such as with searches or pulling user data.\n
    The XML data for updates, adds and other requests are gathered from the following attributes:\n
    - episodes.current -> episode
    - status.user -> status
    - scores.user -> score
    - rewatched.times -> times_rewatched
    - rewatched.value -> rewatch_value
    - storage.type -> storage_type
    - storage.value -> storage_value
    - dates.user.start -> date_start
    - dates.user.end -> date_finish
    - priority -> priority
    - flags.discussion -> boolean to indicate whether it's enabled or disabled
    - flags.rewatching -> boolean to indicate whether it's enabled or disabled
    - comments -> comments
    - fansub_group -> fansub_group
    - tags -> tags
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
        self.status = NT_STATUS(series=kwargs.get('status_anime'), user=kwargs.get('status'))
        self.dates = NT_DATES(series=[kwargs.get('anime_start'), kwargs.get('anime_end')],
                              user=[kwargs.get('date_start'), kwargs.get('date_finish')])
        self.synopsis = kwargs.get('synopsis')
        self.image = kwargs.get('image')
        self.storage = NT_STORAGE(type=kwargs.get('storage_type'), value=kwargs.get('storage_value'))
        self.rewatched = NT_REWATCHED(times=kwargs.get('rewatched'), value=kwargs.get('rewatch_value'))
        self.flags = NT_FLAGS(discussion=kwargs.get('discussion'), rewatching=kwargs.get('rewatching'))
        self.priority = kwargs.get('priority')
        self.comments = kwargs.get('comments')
        self.tags = kwargs.get('tags')
        self.fansub_group = kwargs.get('fansub_group')
        self.xml_tags = ['episodes', 'scores', 'status', 'dates', 'storage', 'rewatched', 'flags', 'priority',
                         'comments', 'tags', 'fansub_group']

    def to_xml(self):
        """
        Convert data to XML String.
        :return: Str of valid XML data
        """
        root = ET.Element("entry")
        for x in self.xml_tags:
            if getattr(self, x):
                if x in ['episodes', 'scores', 'status', 'dates', 'storage', 'rewatched', 'flags', 'tags']:
                    if x == 'episodes':
                        if self.episodes.current:
                            temp = ET.SubElement(root, 'episode')
                            temp.text = str(self.episodes.current)
                    elif x == 'scores':
                        if self.scores.user:
                            temp = ET.SubElement(root, 'score')
                            temp.text = str(self.scores.user)
                    elif x == 'status':
                        if self.status.user:
                            temp = ET.SubElement(root, 'status')
                            temp.text = str(self.status.user)
                    elif x == 'dates':
                        if self.dates.user.start:
                            start = ET.SubElement(root, 'date_start')
                            start.text = self.dates.user.start
                        if self.dates.user.end:
                            end = ET.SubElement(root, 'date_finish')
                            end.text = self.dates.user.end
                    elif x == 'storage':
                        if self.storage.type:
                            stype = ET.SubElement(root, 'storage_type')
                            stype.text = str(self.storage.type)
                        if self.storage.value:
                            sval = ET.SubElement(root, 'storage_value')
                            sval.text = str(self.storage.value)
                    elif x == 'rewatched':
                        if self.rewatched.times:
                            rt = ET.SubElement(root, 'times_rewatched')
                            rt.text = str(self.rewatched.times)
                        if self.rewatched.value:
                            rv = ET.SubElement(root, 'rewatch_value')
                            rv.text = str(self.rewatched.value)
                    elif x == 'flags':
                        if self.flags.discussion:
                            df = ET.SubElement(root, 'enable_discussion')
                            df.text = '1' if self.flags.discussion else '0'
                        if self.flags.rewatching:
                            rf = ET.SubElement(root, 'enable_rewatching')
                            rf.text = '1' if self.flags.rewatching else '0'
                    else:
                        if self.tags:
                            temp = ET.SubElement(root, 'tags')
                            temp.text = ','.join(self.tags)
                else:
                    temp = ET.SubElement(root, x)
                    temp.text = str(getattr(self, x))
        return '<?xml version="1.0" encoding="UTF-8"?>{}'.format(ET.tostring(root, encoding="unicode"))


class Manga:
    """
    An encapsulated Mal Manga Object for updates and adds.\n
    These can be created by the programmer or by the library, such as with searches or pulling user data.\n
    The XML data for updates, adds and other requests are gathered from the following attributes:\n
    - chapters.current -> chapter
    - volumes.current -> volume
    - status.user -> status
    - scores.user -> score
    - reread.times -> times_reread
    - reread.value -> reread_value
    - storage.type -> storage_type
    - storage.value -> storage_value
    - dates.user.start -> date_start
    - dates.user.end -> date_finish
    - priority -> priority
    - flags.discussion -> boolean to indicate whether it's enabled or disabled
    - flags.rereading -> boolean to indicate whether it's enabled or disabled
    - comments -> comments
    - scan_group -> scan_group
    - tags -> tags
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
        self.volumes = NT_EPISODES(total=kwargs.get('volumes'), current=kwargs.get('volume'))
        self.scores = NT_SCORES(average=kwargs.get('average'), user=kwargs.get('score'))
        self.type = kwargs.get('type')
        self.status = NT_STATUS(series=kwargs.get('status_manga'), user=kwargs.get('status'))
        self.dates = NT_DATES(series=[kwargs.get('manga_start'), kwargs.get('manga_end')],
                              user=[kwargs.get('date_start'), kwargs.get('date_finish')])
        self.synopsis = kwargs.get('synopsis')
        self.image = kwargs.get('image')
        self.storage = NT_STORAGE(type=kwargs.get('storage_type'), value=kwargs.get('storage_value'))
        self.reread = NT_REWATCHED(times=kwargs.get('reread'), value=kwargs.get('reread_value'))
        self.flags = NT_FLAGS(discussion=kwargs.get('discussion'), rereading=kwargs.get('rereading'))
        self.priority = kwargs.get('priority')
        self.comments = kwargs.get('comments')
        self.tags = kwargs.get('tags')
        self.scan_group = kwargs.get('scan_group')
        self.xml_tags = ['id', 'chapters', 'volumes', 'scores', 'status', 'dates', 'storage', 'reread', 'flags',
                         'priority', 'comments', 'tags', 'scan_group']

    def to_xml(self):
        root = ET.Element("entry")
        for x in self.xml_tags:
            if getattr(self, x):
                if x in ['chapters', 'volumes', 'scores', 'status', 'dates', 'storage', 'reread', 'flags', 'tags']:
                    if x == 'chapters':
                        if self.chapters.current:
                            temp = ET.SubElement(root, 'chapter')
                            temp.text = str(self.chapters.current)
                    elif x == 'volumes':
                        if self.volumes.current:
                            temp = ET.SubElement(root, 'volume')
                            temp.text = str(self.volumes.current)
                    elif x == 'scores':
                        if self.scores.user:
                            temp = ET.SubElement(root, 'score')
                            temp.text = str(self.scores.user)
                    elif x == 'status':
                        if self.status.user:
                            temp = ET.SubElement(root, 'status')
                            temp.text = str(self.status.user)
                    elif x == 'dates':
                        if self.dates.user.start:
                            start = ET.SubElement(root, 'date_start')
                            start.text = str(self.dates.user.start)
                        if self.dates.user.end:
                            end = ET.SubElement(root, 'date_finish')
                            end.text = str(self.dates.user.end)
                    elif x == 'storage':
                        if self.storage.type:
                            stype = ET.SubElement(root, 'storage_type')
                            stype.text = str(self.storage.type)
                        if self.storage.value:
                            sval = ET.SubElement(root, 'storage_value')
                            sval.text = str(self.storage.value)
                    elif x == 'reread':
                        if self.reread.times:
                            rt = ET.SubElement(root, 'times_reread')
                            rt.text = str(self.reread.times)
                        if self.reread.value:
                            rv = ET.SubElement(root, 'reread_value')
                            rv.text = str(self.reread.value)
                    elif x == 'flags':
                        if self.flags.discussion:
                            df = ET.SubElement(root, 'enable_discussion')
                            df.text = '1' if self.flags.discussion else '0'
                        if self.flags.rereading:
                            rf = ET.SubElement(root, 'enable_rereading')
                            rf.text = '1' if self.flags.rereading else '0'
                    else:
                        if self.tags:
                            temp = ET.SubElement(root, 'tags')
                            temp.text = ','.join(self.tags)
                else:
                    temp = ET.SubElement(root, x)
                    temp.text = str(getattr(self, x))
        return '<?xml version="1.0" encoding="UTF-8"?>{}'.format(ET.tostring(root, encoding="unicode"))


class User:
    """
    An encapsualted object for a User on MyAnimeList. This is never created directly, rather it is made internally.
    """

    def __init__(self, **kwargs):
        """
        Creates the initial data object. Has the following params.

        :param str id: User ID
        :param str name: User Name
        :param NT_TYPEDATA anime: A namedtuple containing a list and stats attribute. List contains a list of :class:`Pymoe.Mal.Objects.Anime` objects and stats contains anime stats for the user.
        :param NT_TYPEDATA manga: A namedtuple containing a list and stats attribute. List contains a list of :class:`Pymoe.Mal.Objects.Manga` objects and stats contains manga stats for the user.
        """
        self.id = kwargs.get('uid')
        self.name = kwargs.get('name')
        self.anime = NT_TYPEDATA(list=kwargs.get('anime_list'), stats=NT_STATS(completed=kwargs.get('anime_completed'),
                                                                               onhold=kwargs.get('anime_onhold'),
                                                                               dropped=kwargs.get('anime_dropped'),
                                                                               planned=kwargs.get('anime_planned'),
                                                                               current=kwargs.get('anime_watching'),
                                                                               days=kwargs.get('anime_days')))
        self.manga = NT_TYPEDATA(list=kwargs.get('manga_list'), stats=NT_STATS(completed=kwargs.get('manga_completed'),
                                                                               onhold=kwargs.get('manga_onhold'),
                                                                               dropped=kwargs.get('manga_dropped'),
                                                                               planned=kwargs.get('manga_planned'),
                                                                               current=kwargs.get('manga_watching'),
                                                                               days=kwargs.get('manga_days')))
