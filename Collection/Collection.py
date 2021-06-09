class Collection():
    def __init__(self, vType):
        self.__vType = vType
        self.__cache = dict()
        self.__size = 0

    def set(self, key: str, value):
        if isinstance(value, self.__vType) is False:
            raise Exception("The value does not match the specified type.")

        self.__cache[key] = value
        return value

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
        return self.__cache.items()

    def keys(self) -> 'iter':
        return iter(self.__cache.keys())

    def values(self) -> 'iter':
        return iter(self.__cache.values())

    def for_each(self,fn):
        for k,v in self.entries():
            fn(k,v,self)
