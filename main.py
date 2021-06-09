
class Collection():
    def __init__(self, V):
        self.__cache = dict()
        self.__vType = V

    def set(self, key: str, value):
        if isinstance(value, self.__vType) is False:
            raise Exception("k")
        self.__cache[key] = value

    def get(self, key: str):
        try:
            return self.__cache[key]
        except:
            return None

    def has(self, key: str):
        try:
            self.__cache[key]
            return True
        except:
            return False


coll = Collection(str)

coll.set("otbir", "31")
coll.set("otozbir", 31)
print(coll.get("hi"))
