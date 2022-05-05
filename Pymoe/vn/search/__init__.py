import pymoe.vn.connection
from pymoe.helpers import vndbWrapper

def vn(term: str, page: int = 1):
    """
        TODO: Write This
    """
    ret = pymoe.vn.connection.mySock.send_command("get vn basic,anime,details,stats,screens (title ~ {})".format(term))
    
    if ret['more']:
        return vndbWrapper(
            ret['items'],
            pymoe.vn.connection.mySock,
            page+1,
            "get vn basic,anime,details,stats,screens (title ~ {})".format(term)
        )
    else:
        return vndbWrapper(
            ret['items'],
            pymoe.vn.connection.mySock,
            None,
            None
        )
    

def character(term: str, page: int = 1):
    """
        TODO: Write This
    """
    ret = pymoe.vn.connection.mySock.send_command("get character basic,details,meas,vns (search ~ {})".format(term))

    if ret['more']:
        return vndbWrapper(
            ret['items'],
            pymoe.vn.connection.mySock,
            page+1,
            "get character basic,details,meas,vns (search ~ {})".format(term)
        )
    else:
        return vndbWrapper(
            ret['items'],
            pymoe.vn.connection.mySock,
            None,
            None
        )
        

def releases(vnid: int, page: int = 1):
    """
        TODO: Write This
    """
    ret = pymoe.vn.connection.mySock.send_command("get release basic,details (vn = {})".format(vnid))

    if ret['more']:
        return vndbWrapper(
            ret['items'],
            pymoe.vn.connection.mySock,
            page+1,
            "get release basic,details (vn = {})".format(vnid)
        )
    else:
        return vndbWrapper(
            ret['items'],
            pymoe.vn.connection.mySock,
            None,
            None
        )