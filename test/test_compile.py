

def test_compile():
    try:
        import tiddlywebplugins.imaker
        assert True
    except ImportError as exc:
        assert False, exc
