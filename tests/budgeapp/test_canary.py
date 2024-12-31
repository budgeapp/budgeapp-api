from importlib import metadata


def test_canary():
    assert metadata.metadata("budgeapp")["Name"] == "budgeapp"
