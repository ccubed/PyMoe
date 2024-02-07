import pymoe.ln.get.bakatsuki as bakatsuki
import pymoe.ln.get.wlnupdates as wlnupdates

"""
    Default methods with WLNUpdates
"""

def series(item_id : int):
    """
        Default get series method from WLNUpdates
    """
    return wlnupdates.series(item_id)

def artist(item_id : int):
    """
        Default get artist method from WLNUpdates
    """
    return wlnupdates.artist(item_id)

def author(item_id : int):
    """
        Default get author method from WLNUpdates
    """
    return wlnupdates.author(item_id)

def group(item_id : int):
    """
        Default get group method from WLNUpdates
    """
    return wlnupdates.group(item_id)

def publisher(item_id : int):
    """
        Default get publisher method from WLNUpdates
    """
    return wlnupdates.publisher(item_id)

def genre(item_id : int):
    """
        Default get genre method from WLNUpdates.
        NOTICE: This will return all items with that genre.
    """
    return wlnupdates.genre(item_id)

def tag(item_id : int):
    """
        Default get tag method from WLNUpdates.
        NOTICE: This will return all items with that tag.
    """
    return wlnupdates.tag(item_id)