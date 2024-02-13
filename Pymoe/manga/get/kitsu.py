import requests
import ujson
from pymoe.utils.errors import serializationFailed, serverError

settings = {
    "header": {
        "Content-Type": "application/vnd.api+json",
        "User-Agent": "Pymoe (github.com/ccubed/PyMoe)",
        "Accept": "application/vnd.api+json",
    },
    "apiurl": "https://kitsu.io/api/edge",
}


def manga(item_id: int):
    """
    Get information on the given manga by ID.

    :param item_id: The ID of the manga you want information on
    """
    r = requests.get(
        settings["apiurl"] + "/manga/{}".format(item_id), headers=settings["header"]
    )

    if r.status_code != 200:
        if r.status_code == 404:
            return None
        else:
            raise serverError(r.text, r.status_code)

    try:
        jsd = ujson.loads(r.text)
    except ValueError:
        raise serializationFailed(r.text, r.status_code)
    else:
        return jsd
