from bullsandcows import isdebugmode

def test_isdebugmode():
    assert isdebugmode() == 0, "program is in debug mode, this should not be commited"
