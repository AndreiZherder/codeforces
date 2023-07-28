fac_mem = [1]
def fac(n, cache=True):
    if not cache:
        r = 1
        for i in range(1, n + 1):
            r = (r * i) % MOD
        return r
    else:
        while len(fac_mem) < n + 1:
            fac_mem.append(fac_mem[-1] * len(fac_mem) % MOD)
        return fac_mem[n]
def perm(n, k, cache=True):
    return fac(n, cache=cache) * inv(fac(k, cache=cache)) % MOD
def comb(n, k, cache=True):
    return fac(n, cache=cache) * inv(fac(k, cache=cache) * fac(n - k, cache=cache)) % MOD


import sys, time, random
from collections import deque, Counter, defaultdict

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 2 ** 63 - 1


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


class Cumsum1d():
    def __init__(self, A):
        self.n = len(A)
        self.Suma = [0] * (self.n + 1)
        for i in range(self.n):
            self.Suma[i + 1] += self.Suma[i] + A[i]

    def query(self, l, r):
        # 0-indexed
        return self.Suma[r] - self.Suma[l]

    def get(self, i):
        return self.Suma[i + 1] - self.Suma[i]

    def __getitem__(self, p):
        if isinstance(p, int):
            return self.get(p)
        else:
            return self.query(p.start, p.stop)


def solve():
    n, m = mi()
    s = input()
    A = Cumsum1d(list(map(int, s)))
    base = random.randint(1, mod - 1)
    S = Rollinghash(s, base, mod)
    zero = Rollinghash('0' * n, base, mod)
    one = Rollinghash('1' * n, base, mod)
    ans = set()

    for i in range(m):
        l, r = mi()
        l -= 1
        c1 = A[l:r]
        c0 = r - l - c1
        ss = S.query(0, l) * S.pow[n - l] + zero.query(0, c0) * S.pow[n - l - c0] + one.query(0, c1) * S.pow[
            n - l - c0 - c1] + S.query(r, n)
        ss %= mod
        ans.add(ss)

    print(len(ans))


for _ in range(ii()):
    solve()



if path.exists("/Users/arijitbhaumik/Library/Application Support/Sublime Text/Packages/User/input.txt"):
        sys.stdin = open("/Users/arijitbhaumik/Library/Application Support/Sublime Text/Packages/User/input.txt", 'r')
        sys.stdout = open("/Users/arijitbhaumik/Library/Application Support/Sublime Text/Packages/User/output.txt", 'w')