import pymoe.vn.connection

def vn(vnid: int):
    """
        Given an ID for a Visual Novel from VNDB, return information on that Visual Novel.

        :param vnid: The ID of the Visual Novel
    """
    ret = pymoe.vn.connection.mySock.send_command("get vn basic,anime,details,stats,screens (id = {})".format(vnid))
    return ret['items']

def release(rlsid: int):
    """
        Given an ID for a release from VNDB, return information on that release.

        :param rlsid: The ID of the Release
    """
    ret = pymoe.vn.connection.mySock.send_command("get release basic,details (id = {})".format(rlsid))
    return ret['items']

def character(cid: int):
    """
        Given an ID for a character from VNDB, return information on that character.

        :param cid: The ID of the Character
    """
    ret = pymoe.vn.connection.mySock.send_command("get character basic,details,meas,vns (id = {})".format(cid))
    return ret['items']