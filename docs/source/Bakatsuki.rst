Bakatsuki
=========

Welcome to the Bakatsuki implementation. This Implementation is made entirely using the Mediawiki API and allows you to query against the current and past Bakatsuki translation projects.

Methods
-------

.. py:function:: active()

    Returns a list of tuples in the format (title, pageid) for all the projects currently in the active category.

.. py:function:: light_novels(language : string = "English")

    Language should be one of the languages available on the site list. Defaults to English. For an Idea of what to put here, click on another language of light novels and look for the value in ( and ).

    Returns a list of tuples in the format (title, pageid) that list the light novels in the given language.

.. py:function:: teaser(language : string = "English")

    Language should be one of the languages available on the site list. Defaults to English. For an Idea of what to put here, click on another language of teaser projects and look for the value in ( and ).

    Returns a list of tuples in the format (title, pageid) that list the current teaser projects for the given language.

.. py:function:: web_novels(language : string = "English")

    Language should be one of the languages available on the site list. Defaults to English. For an Idea of what to put here, click on another language of web novels and look for the value in ( and ).

    Returns a list of tuples in the format (title, pageid) that list the current web novels for the given language.

.. py:function:: chapters(title : string)

    Return an OrderedDict which contains the chapters found for the visual novel specified. This OrderedDict contains tuples of (url, title). It is ordered by chapter # and then sub chapter. This should be the title given from one of the above functions.

.. py:function:: cover(pageid : string)

    Return a url to the cover image used for the given visual novel at the given pageid. Use the pageid's given in one of the above functions.

.. py:function:: get_text(title : string)

    Return the html content for a given chapter given the title as given by the chapters function above. You'll have to parse the HTML yourself or throw it into a disposable web control.

    Yes, you can use this to get the html content of other pages too.