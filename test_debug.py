from bullsandcows import isdebug

def test_isdebug():
    assert isdebug() == 0, "program is in debug mode, this should not be commited"
