from random import randint


class Collection():
    def __init__(self, vType, *collections: tuple):
        self.__vType = vType
        self.__cache = dict()
        self.__size = 0
        if len(collections) > 0:
            for collection in collections:
                for k, v in collection.entries():
                    self.set(k, v)

    def set(self, key: str, value):
        if isinstance(value, self.__vType) is False:
            raise Exception("The value does not match the specified type.")

        self.__cache[key] = value
        return self

    def get(self, key: str):
        return self.__cache.get(key)

    def get_size(self) -> int:
        return len(self.__cache)

    def has(self, key: str):
        if self.__cache.get(key) is not None:
            return True

        return False

    def clear(self) -> 'Collection':
        self.__cache.clear()
        return self

    def delete(self, key: str):
        try:
            del self.__cache[key]
            return True
        except:
            return False

    def __iter__(self):
        return self.__cache.__iter__()

    def entries(self):
        result = []

        for k in self.key_list():
            result.append([k, self.get(k)])

        return result

    def keys(self) -> 'iter':
        return iter(self.__cache.keys())

    def values(self) -> 'iter':
        return iter(self.__cache.values())

    def for_each(self, fn):
        for k, v in self.entries():
            fn(v, k, self)
        return None

    def map(self, fn):
        result = []

        for k, v in self.entries():
            result.append(fn(v, k, self))
        return result

    def filter(self, fn):
        result = Collection(self.__vType)

        for k, v in self.entries():
            if fn(v, k, self) == True:
                result.set(k, v)

        return result

    def some(self, fn) -> bool:
        for k, v in self.entries():
            if fn(v, k, self) == True:
                return True

        return False

    def every(self, fn) -> bool:
        for k, v in self.entries():
            if fn(v, k, self) == False:
                return False

        return True

    def equals(self, collection: 'Collection') -> bool:
        if collection.get_size() is not self.get_size():
            return False

        for k, v in collection.entries():
            if v == self.get(k):
                return True

        return False

    def clone(self) -> 'Collection':
        return Collection(self.__vType, self)

    def concat(self, *collections: tuple):
        if len(collections) == 0:
            return self

        clone = self.clone()

        for collection in collections:
            for k, v in collection.entries():
                clone.set(k, v)

        return clone

    def difference(self, other: 'Collection') -> 'Collection':
        clone = Collection(self.__vType)

        for k, v in self.entries():
            if other.has(k) == False:
                clone.set(k, v)
                print(k)

        for k, v in other.entries():
            if self.has(k) == False:
                clone.set(k, v)

        return clone

    def each(self, fn):
        self.for_each(fn)
        return self

    def find_key(self, fn):
        for k, v in self.entries():
            if fn(v, k, self) == True:
                return k

        return None

    def find_value(self, fn):
        for k, v in self.entries():
            if fn(v, k, self) == True:
                return v

        return None

    def first(self, amount=None):
        _iter = self.values()

        if amount == None:
            return next(_iter)

        if amount < 0:
            return self.last(amount * -1)

        amount = min(self.get_size(), amount)

        result = list()

        for n in range(amount):
            result.append(next(_iter))

        return result

    def first_key(self, amount=None):
        _iter = self.keys()

        if amount == None:
            return next(_iter)

        if amount < 0:
            return self.last_key(amount * -1)

        amount = min(self.get_size(), amount)

        result = list()

        for n in range(amount):
            result.append(next(_iter))

        return result

    def last(self, amount=None):
        values = list(self.values())

        if amount == None:
            return values[len(values) - 1]

        if amount < 0:
            return self.first(amount * -1)

        amount = min(self.get_size(), amount)

        return values[-amount:]

    def last_key(self, amount=None):
        keys = list(self.keys())

        if amount == None:
            return keys[len(keys) - 1]

        if amount < 0:
            return self.first_key(amount * -1)

        amount = min(self.get_size(), amount)

        return keys[-amount:]

    def to_list(self) -> list:
        return list(self.values())

    def key_list(self) -> list:
        return list(self.keys())

    def flat_map(self, fn):
        result_collection = Collection(self.__vType)

        result = self.map(fn)

        for e in result:
            if isinstance(e, Collection):
                for k, v in e.entries():
                    result_collection.set(k, v)

        return result_collection

    def intersect(self, other: 'Collection') -> 'Collection':
        def fn(_v, k, _c):
            return self.has(k)

        return other.filter(fn)

    def map_values(self, fn) -> 'Collection':
        result = Collection(self.__vType)

        for k, v in self.entries():
            result.set(k, fn(v, k, self))

        return result

    def partition(self, fn) -> list:
        result = [
            Collection(self.__vType),
            Collection(self.__vType)
        ]

        for k, v in self.entries():
            if fn(v, k, self) == True:
                result[0].set(k, v)
            else:
                result[1].set(k, v)

        return result

    def random(self, amount=None):
        values = self.to_list()

        if amount == None:
            return values[randint(0, self.get_size() - 1)]

        result = []

        for n in range(amount):
            result.append(self.random())

        return result

    def random_key(self, amount=None):
        keys = self.key_list()

        if amount == None:
            return keys[randint(0, self.get_size() - 1)]

        result = []

        for n in range(amount):
            result.append(self.random_key())

        return result

    def reduce(self, fn, initalValue=None):
        accumulator = None

        if initalValue is not None:
            accumulator = initalValue

            for k, v in self.entries():
                accumulator = fn(accumulator, v, k, self)

            return accumulator

        first = True

        for k, v in self.entries():
            if first == True:
                accumulator = fn(accumulator, v, k, self)
                first = False
            else:
                accumulator = fn(accumulator, v, k, self)

        return accumulator

    def sweep(self, fn) -> int:
        total = 0

        for k, v in self.entries():
            if fn(v, k, self) == True:
                self.delete(k)
                total += 1

        return total

    def tap(self, fn):
        fn(self)
        return self
