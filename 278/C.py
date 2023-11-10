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
    d = defaultdict(list)
    for i in range(n):
        k, *a = [int(num) for num in input().split()]
        for ai in a:
            d[ai].append(i)
    if not d:
        print(n)
        return
    dsu = DSU(n)
    for vs in d.values():
        for i in range(1, len(vs)):
            dsu.union(vs[i - 1], vs[i])
    print(len({dsu.find(i) for i in range(n)}) - 1)



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
