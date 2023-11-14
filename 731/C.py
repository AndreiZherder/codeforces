from collections import defaultdict, Counter
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
    n, m, k = [int(num) for num in input().split()]
    c = [int(num) for num in input().split()]
    dsu = DSU(n)
    for i in range(m):
        v, u = [int(num) - 1 for num in input().split()]
        dsu.union(v, u)
    d = defaultdict(list)
    for v in range(n):
        d[dsu.find(v)].append(v)
    ans = 0
    for vs in d.values():
        cnt = Counter()
        for v in vs:
            cnt[c[v]] += 1
        mx = max(cnt.values())
        ans += len(vs) - mx
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
