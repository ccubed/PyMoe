import pymoe.ln.search.bakatsuki as bakatsuki
import pymoe.ln.search.wlnupdates as wlnupdates

# Default search method with WLNUpdates


def series(title: str):
    """
    Return a title search for title against WLNUpdates
    """
    return wlnupdates.series(title)
