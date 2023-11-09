from collections import defaultdict
from os import path
from sys import stdin, stdout


filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


class DSU:
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        id1 = self.find(i)
        id2 = self.find(j)
        if id1 == id2:
            return
        if self.rank[id1] > self.rank[id2]:
            self.parent[id2] = id1
        else:
            self.parent[id1] = id2
            if self.rank[id1] == self.rank[id2]:
                self.rank[id2] += 1


def solution():
    n, m = [int(num) for num in input().split()]
    g = [[] for i in range(n)]
    dsu1 = DSU(n)
    for i in range(m):
        v, u = [int(num) for num in input().split()]
        v -= 1
        u -= 1
        g[v].append(u)
        g[u].append(v)
        dsu1.union(v, u)

    components = defaultdict(list)
    for v in range(n):
        components[dsu1.find(v)].append(v)


    k1 = 0
    k2 = 0
    ans1 = []
    ans2 = []

    for vs in components.values():
        dsu = DSU(len(vs))
        d = {v: i for i, v in enumerate(vs)}
        for v in vs:
            us = g[v]
            id_v = dsu.find(d[v])
            if us:
                if id_v == dsu.find(d[us[0]]):
                    print(-1)
                    return
                for i in range(1, len(us)):
                    if id_v == dsu.find(d[us[i]]):
                        print(-1)
                        return
                    dsu.union(d[us[i]], d[us[i - 1]])
        s = list({dsu.find(d[v]) for v in vs})
        for v in vs:
            if dsu.find(d[v]) == s[0]:
                k1 += 1
                ans1.append(v + 1)
            else:
                k2 += 1
                ans2.append(v + 1)
    print(k1)
    print(*ans1)
    print(k2)
    print(*ans2)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
