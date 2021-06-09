class Collection():
    def __init__(self, vType):
        self.__vType = vType
        self.__cache = dict()

    def set(self, key: str, value):
        if isinstance(value, self.__vType) is False:
            raise Exception("The value does not match the specified type.")

        self.__cache[key] = value
        return value

    def get(self, key: str):
        try:
            return self.__cache[key]
        except:
            return None
