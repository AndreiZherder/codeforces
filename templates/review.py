from typing import Tuple


def imap():  # Multiple numbers input
    return map(int, input().split())


def ilist():  # List input
    return list(map(int, input().split()))


def ilgraph(n, m):  # Graph input as Adjacency List

    l = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = imap()
        l[x].append(y)
        l[y].append(x)
    return l


def iagraph(n, m):  # Graph input as Adjacency Matrix
    l = [[0 for i in range(n + 1)] for i in range(n + 1)]
    for i in range(m):
        x, y = imap()
        l[x][y] = 1
        l[y][x] = 1
    return l


def base_change(nn, bb):
    if nn == 0:
        return [0]
    digits = []
    while nn:
        digits.append(int(nn % bb))
        nn //= bb
    return digits[::-1]





# source?
class fenwTree:  # used for prefix operations
    def __init__(self, a, func=lambda a, b: a + b):
        self.a = a
        self.func = func
        self.arr = [0] * (len(a) + 1)
        for i in range(len(a)):
            self.buildTree(i, a[i])

    def buildTree(self, idx, val):
        idx += 1  # make it a 1-based indexing
        while idx <= len(self.a):
            self.arr[idx] = self.func(self.arr[idx], val)
            idx += idx & (-idx)

    def update(self, idx, val):
        idx += 1  # make it a 1-based indexing
        diff = val - self.a[idx - 1]
        self.a[idx - 1] = val
        while idx <= len(self.a):
            self.arr[idx] = self.func(self.arr[idx], diff)
            idx += idx & (-idx)

    def query(self, idx):
        idx += 1
        ans = 0
        while idx > 0:
            ans = self.func(ans, self.arr[idx])
            idx -= idx & (-idx)
        return ans


# Source ?
class segTree:
    def __init__(self, arr, func=max):
        self.arr = arr
        self.func = func
        self.n = len(self.arr)
        self.tree = [0] * (4 * (self.n))
        self.buildTree(0, self.n - 1, 0)

    def buildTree(self, ss, se, si):
        if (ss == se):
            self.tree[si] = self.arr[ss]
            return self.tree[si]
        mid = (ss + se) // 2
        self.tree[si] = self.func(self.buildTree(ss, mid, (2 * si) + 1), self.buildTree(mid + 1, se, (2 * si) + 2))
        return self.tree[si]

    def queryFunc(self, qs, qe, ss, se, si):
        if (ss > qe or se < qs):
            return 0
        if (ss >= qs and se <= qe):
            return self.tree[si]
        mid = (ss + se) // 2
        return self.func(self.queryFunc(qs, qe, ss, mid, (2 * si) + 1),
                         self.queryFunc(qs, qe, mid + 1, se, (2 * si) + 2))

    def query(self, qs, qe):
        return self.queryFunc(qs, qe, 0, self.n - 1, 0)

    def updateFunc(self, idx, diff, ss, se, si):
        if (idx < ss or idx > se):
            return self.tree[si]
        if (ss == se and idx == ss):
            self.tree[si] += diff
            return self.tree[si]
        if (se > ss):
            mid = (ss + se) // 2
            self.tree[si] = self.func(self.updateFunc(idx, diff, ss, mid, (2 * si) + 1),
                                      self.updateFunc(idx, diff, mid + 1, se, (2 * si) + 2))
        return self.tree[si]

    def update(self, idx, val):
        k = val - self.arr[idx]
        self.arr[idx] = val
        self.updateFunc(idx, k, 0, self.n - 1, 0)







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