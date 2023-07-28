from random import randint

mod = 1000000007
base = randint(1, mod - 1)


class Rollinghash:
    def __init__(self, string, base, mod):
        n = len(string)
        self.__base = base
        self.__mod = mod
        self.__hash = [0] * (n + 1)
        self.__pow = [1] * (n + 1)
        if isinstance(string, str):
            for i, c in enumerate(string):
                o = ord(c) - ord('a') + 1
                self.__hash[i + 1] = (self.__hash[i] * self.__base + o) % self.__mod
                self.__pow[i + 1] = self.__pow[i] * self.__base % self.__mod
        else:
            for i, c in enumerate(string):
                o = c
                self.__hash[i + 1] = (self.__hash[i] * self.__base + o) % self.__mod
                self.__pow[i + 1] = self.__pow[i] * self.__base % self.__mod
        self.pow = self.__pow[:]

    def query(self, l, r):
        ret = (self.__hash[r] - self.__hash[l] * self.__pow[r - l]) % self.__mod
        return ret

    def same(self, l1, r1, l2, r2):
        return self.query(l1, r1) == self.query(l2, r2)
