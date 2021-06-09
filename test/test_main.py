from Collection.Collection import Collection
import pytest

coll = Collection(int)

v = coll.set("test", 3)


def test_set():
    assert v == coll


def test_get():
    assert coll.get("test") == 3


def test_get_none():
    assert coll.get("testNone") == None


def test_get_size():
    assert coll.get_size() == 1


def test_has():
    assert coll.has("test") == True


def test_has_with_false():
    assert coll.has("testNone") == False


def test_clear():
    assert coll.clear().get_size() == 0


def test_delete():
    coll.set("test", 3)
    assert coll.delete("test") == True


def test_delete_with_not_exist():
    assert coll.delete("test") == False


def test_iter():
    coll.set("test", 3)
    for item in coll:
        assert item == "test"


def test_entries():
    for k, v in coll.entries():
        assert k == "test"
        assert v == 3


def test_keys():
    assert next(coll.keys()) == "test"


def test_values():
    assert next(coll.values()) == 3


def test_for_each():
    def fn(v, k, c):
        assert k == "test"
        assert v == 3
        assert c == coll

    coll.for_each(fn)


def test_map():
    def fn(v, k, c):
        return v * 2

    assert coll.map(fn) == [6]


def test_filter():
    def fn(v, k, c):
        return v == 3
    assert coll.filter(fn).get_size() == coll.get_size()


def test_some():
    def fn(v, k, c):
        return v == 3 and k == "test"
    assert coll.some(fn) == True


def test_every():
    coll.set("testSecond", 4)

    def fn(v, k, c):
        return v == 3

    assert coll.every(fn) == False


def test_equal():
    coll2 = coll.clone()

    assert coll.equals(coll2) == True


def test_concat():
    coll2 = Collection(int)
    for n in range(10):
        coll2.set(str(n), n)

    concat = coll.concat(coll2)

    assert concat.get_size() == 12


def test_difference():
    coll2 = Collection(int)
    coll3 = Collection(int)
    for n in range(10):
        coll2.set(str(n), n)

    for n in range(15):
        coll3.set(str(n), n)

    assert coll2.difference(coll3).get_size() == 5


def test_each():
    def fn(v, k, c):
        assert c == coll

    coll.each(fn)


def test_find_key():
    def fn(v, k, c):
        return k == "test"

    assert coll.find_key(fn) == "test"


def test_find_value():
    def fn(v, k, c):
        return k == "test"

    assert coll.find_value(fn) == 3


def test_first_without_amount():
    assert coll.first() == 3


def test_first_with_amount():
    assert coll.first(5) == [3, 4]


def test_first_with_negative_amount():
    coll.set("added", 5)
    assert coll.first(-2) == [4, 5]


def test_last_without_amount():
    assert coll.last() == 5


def test_last_with_amount():
    coll.clear()
    for n in range(10):
        coll.set(str(n), n)

    assert coll.last(2) == [8, 9]


def test_last_with_negative_amount():
    assert coll.last(-2) == [0, 1]


def test_first_key_without_amount():
    assert coll.first_key() == "0"


def test_first_key_with_amount():
    assert coll.first_key(2) == ["0", "1"]


def test_first_key_with_negative_amount():
    assert coll.first_key(-2) == ["8", "9"]


def test_last_key_without_amount():
    assert coll.last_key() == "9"


def test_last_key_with_amount():
    assert coll.last_key(2) == ["8", "9"]


def test_last_key_with_negative_amount():
    assert coll.last_key(-2) == ["0", "1"]


def test_to_list():
    coll.clear()
    coll.set("0", 0)
    coll.set("1", 1)

    assert coll.to_list() == [0, 1]


def test_key_list():
    assert coll.key_list() == ["0", "1"]


def test_flat_map():
    coll2 = Collection(int)

    def fn(v, k, c):
        return coll2.set(k, v)

    assert coll.flat_map(fn).equals(coll2) == True


def test_intersect():

    clone = coll.clone()
    clone.clear()

    for n in range(2, 5):
        clone.set(str(n), n)

    coll.clear()
    for n in range(5):
        coll.set(str(n), n)

    assert clone.get_size() == 3


def test_map_values():
    result = coll.map_values(lambda v, _, _c: v)

    assert coll.equals(result) == True


def test_partition():
    result = coll.partition(lambda v, _k, _c: v < 3)

    assert result[0].equals(result[1]) == False


def test_reduce():
    coll.clear()

    for n in range(5):
        coll.set(str(n), n)

    assert coll.reduce(lambda a, v, _k, _c: a + v, 0) == 10


def test_sweep():
    assert coll.sweep(lambda v, _k, _c: v < 10) == 5
