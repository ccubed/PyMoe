import pymoe.vn.connection

def vn(vnid: int):
    """
        TODO: Write This
    """
    ret = pymoe.vn.connection.mySock.send_command("get vn basic,anime,details,stats,screens (id = {})".format(vnid))
    return ret['items']

def release(rlsid: int):
    """
        TODO: Write This
    """
    ret = pymoe.vn.connection.mySock.send_command("get release basic,details (id = {})".format(rlsid))
    return ret['items']

def character(cid: int):
    """
        TODO: Write This
    """
    ret = pymoe.vn.connection.mySock.send_command("get character basic,details,meas,vns (id = {})".format(cid))
    return ret['items']