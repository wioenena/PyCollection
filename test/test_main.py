from Collection.Collection import Collection
import pytest

coll = Collection(int)

v = coll.set("test", 3)


def test_set():
    assert v == 3


@pytest.mark.skip
def test_set_err():
    assert v == 4


def test_get():
    assert coll.get("test") == 3


def test_get_none():
    assert coll.get("testNone") == None


@pytest.mark.skip
def test_get_err():
    assert coll.get("test") == 4


def test_get_size():
    assert coll.get_size() == 1


@pytest.mark.skip
def test_get_size_err():
    assert coll.get_size() == 2


def test_has():
    assert coll.has("test") == True


def test_has_with_false():
    assert coll.has("testNone") == False


@pytest.mark.skip
def test_has_err():
    assert coll.has("testNone") == True


def test_clear():
    assert coll.clear().get_size() == 0


@pytest.mark.skip
def test_clear_err():
    assert coll.clear().get_size() == 1


def test_delete():
    coll.set("test", 3)
    assert coll.delete("test") == True


def test_delete_with_not_exist():
    assert coll.delete("test") == False


@pytest.mark.skip
def test_delete_err():
    assert coll.delete("test") == True


def test_iter():
    coll.set("test", 3)
    for item in coll:
        assert item == "test"


@pytest.mark.skip
def test_iter_err():
    for item in coll:
        assert item == "error"


def test_entries():
    for k, v in coll.entries():
        assert k == "test"
        assert v == 3


@pytest.mark.skip
def test_entries_error():
    for k, v in coll.entries():
        assert k == 3
        assert v == "test"


def test_keys():
    assert next(coll.keys()) == "test"


@pytest.mark.skip
def test_keys_err():
    assert next(coll.keys()) == 3


def test_values():
    assert next(coll.values()) == 3


@pytest.mark.skip
def test_values_err():
    assert next(coll.values()) == "test"


def test_for_each():
    def fn(k, v, c):
        assert k == "test"
        assert v == 3
        assert c == coll
    coll.for_each(fn)


@pytest.mark.skip
def test_for_each_err():
    def fn(k, v, c):
        assert k == 3
        assert v == coll
        assert c == "test"
    coll.for_each(fn)
