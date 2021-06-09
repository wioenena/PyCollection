from Collection.Collection import Collection
import pytest

coll = Collection(int)

v = coll.set("test", 3)


def test_set():
    assert v == 3


@pytest.mark.skip
def test_set_err():
    assert v == 4  # Error
