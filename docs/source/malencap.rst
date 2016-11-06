Mal Encapsulations
==================
Welcome to the giant file of MyAnimeList Encapsulations. Get cozy, i'm going to take you on a journey.

The Structures
--------------
These are the files found in Abstractions.py. Mostly they're small pieces of information that should be related and are muxed together to make it easier to interact with.

.. py:class:: NT_EPISODES

    This is used for anime to store current and total episodes, but also for manga to store chapters and volumes.

    .. py:attribute:: current : int

        Current Episodes/Chapters/Volumes Watched/Read
    .. py:attribute:: total : int

        Total Episodes/Chapters/Volumes for this Anime/Manga

.. py:class:: NT_SCORES

    This is used to store score data for Anime and Manga. In the user endpoint, average will be None.

    .. py:attribute:: average : int

        The average rating for this anime or manga

    .. py:attribute:: user : int

        The user's rating for this anime or manga

.. py:class:: NT_STATUS

    This is an abstraction for status data.

    .. py:attribute:: series : string

        The status of the series

    .. py:attribute:: user : string

        The user's status for this series

.. py:class:: NT_DATES

    This is an abstraction for the start and end dates for users and series. The API sends dates in YYYY-MM-DD format.

    .. py:attribute:: series : NT_DATE_OBJ

        Series start and end date. If not available the API returns 0000-00-00.

    .. py:attribute:: user : NT_DATE_OBJ

        User's start and end date. If not available the API returns 0000-00-00.

.. py:class:: NT_DATE_OBJ

    Holds the actual start and end date. An abstraction within an Abstraction! Crazy!

    .. py:attribute:: start : string

    .. py:attribute:: end : string

.. py:class:: NT_STORAGE

    Storage Type and Value abstraction. Type holds the type of storage and value the 'size' parameter of the given storage type if appropriate. At the moment, this isn't actually returned in any API calls, but you can use the API to modify it!

    .. py:attribute:: type : int

        Which storage type.

    .. py:attribute:: value : int

        How much exactly does it take.

.. py:class:: NT_REWATCHED

    This holds your rewatch/reread times and how rewatchable/rereadable a series is.

    .. py:attribute:: times : int

        Times rewatched/reread.

    .. py:attribute:: value : int

        On a scale of 1-5, with 5 being the best, how rewatchable/rereadable is this series?

.. py:class:: NT_FLAGS

    Just holds those random profile flags for each anime and manga.

    .. py:attribute:: discussion : bool

        Are you allowing discussion on the episodes/chapters/volumes you watch/read?

    .. py:attribute:: rewatching : bool

        Are you currently rewatching this series? This value is ignored on manga.

    .. py:attribute:: rereading : bool

        Are you currently rereading this series? This value is ignored on anime.

.. py:class:: NT_TYPEDATA

    Holds user data for anime and manga along with stats

    .. py:attribute:: list : list

        A list of Anime or Manga objects

    .. py:attribute:: stats : NT_STATS

        Stats data for anime or manga

.. py:class:: NT_STATS

    Holds user stats for anime or manga.

    .. py:attribute:: completed : str

        Number of Anime/Manga completed.

    .. py:attribute:: onhold : str

        Number of Anime/Manga on hold.

    .. py:attribute:: dropped : str

        Number of Anime/Manga dropped.

    .. py:attribute:: planned : str

        Number of Anime/Manga planned.

    .. py:attribute:: current : str

        Number of Anime/Manga currently watching.

    .. py:attribute:: days : str

        Days spent watching/reading anime/manga.


The Big Boys
------------
Now for the big boys. Anime, Manga and User. These are the three you will use the most to interface with the API interface.

.. py:class:: Anime

    .. py:attribute:: aid : string

        The MAL ID of the anime.

    .. py:attribute:: title : string

        The title of the anime. In rare cases this can be None.

    .. py:attribute:: synonyms : list

        A list of the alternative titles, if any, for this anime.

    .. py:attribute:: episodes : NT_EPISODES

        current and total episodes for this anime. On add and update requests, current is used for the episode XML parameter.

    .. py:attribute:: scores : NT_SCORES

        Average and User ratings for the anime. Average will only be populated on a search call. The user attribute is used for the score XML parameter.

    .. py:attribute:: type : string

        Type of Anime. Ex: TV, ONA

    .. py:attribute:: status : NT_STATUS

        Stores the status of the series and the user's status for this series. The user attribute is used for the status XML parameter.

    .. py:attribute:: dates : NT_DATES

        Holds the series and user start and end dates. user.start and user.end are the date_start and date_finish for the XML.

    .. py:attribute:: synopsis : string

        If available, here's a synopsis.

    .. py:attribute:: image : string

        If available, here's a link to the image for the anime.

    .. py:attribute:: storage : NT_STORAGE

        Holds storage type and value. type is used for storage_type and value for storage_value as far as XML parameters.

    .. py:attribute:: rewatched : NT_REWATCHED

        Times and value for the rewatched parameters. times is used for times_rewatched and value for rewatch_value as far as XML parameters.

    .. py:attribute:: flags : NT_FLAGS

        Discussion, Rewatching. Are you allowing discussion on your activity with this series and are you rewatching it? These are Bools. Discussion and Rewatching are used for the flags XML Parameter.

    .. py:attribute:: priority : int

        Sets the series priority where 1 is low and 3 is high. 1-3. Used for the priority XML Parameter.

    .. py:attribute:: comments : string

        User comments for the given Anime. Used for the comments XML parameter.

    .. py:attribute:: tags : list

        List of user tags for the anime if available. Used for the tags XML parameter.

    .. py:attribute:: fansub_group : string

        Your fansub group for this anime. Used for the fansub_group XML parameter.

.. py:class:: Manga

    Manga is basically the same as Anime. Instead of relisting every attribute, you should assume Manga has all the attributes in Anime except for those listed here which have been changed.

    .. py:attribute:: mid : int

        Manga's version of AID. The MAL ID for this Manga.

    .. py:attribute:: chapters : NT_EPISODES

        Manga's version of Episodes. Current and Total chapters. Current is used for the chapter XML parameter.

    .. py:attribute:: volumes : NT_EPISODES

        Mangas also have volumes. This works just like chapters except it lists volumes. Current is used for the volume XML Parameter.

    .. py:attribute:: status : NT_STATUS

        This doesn't actually differ from Anime, but I wanted to make a note here that the status values are different. So make sure to account for that.

    .. py:attribute:: reread : NT_REWATCHED

        This works just like Anime's rewatched, but is called reread because that makes more sense to a manga object. times is used for times_reread and value for reread_value in terms of XML parameters. They work just like their Anime mirrors.

    .. py:attribute:: flags : NT_FLAGS

        Just a reminder. This works the same way as anime, but this one uses rereading instead of rewatching. Discussion is shared between both.

    .. py:attribute:: scan_group : string

        Your scanlation group for this manga series. Used as the scan_group XML Parameter.

.. py:class:: User

    The real big boy. A user object. Buckle in.

    .. py:attribute:: id : string

        User ID

    .. py:attribute:: name : string

        User Name

    .. py:attribute:: anime : NT_TYPEDATA

        The anime list along with the user's anime stats.

    .. py:attribute:: manga : NT_TYPEDATA

        The manga list along with the user's manga stats.