import pymoe.utils.helpers as ans

def test_b36d():
    # Test pymoe.utils.helpers.base36Decode
    assert ans.base36Decode("pklldyu") == 55665151734