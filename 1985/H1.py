from collections import Counter
from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
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


    def num(i: int, j: int) -> int:
        return i * m + j


    def solve_for_row(i: int) -> int:
        total = 0
        seen = set()
        if i + 1 < n:
            for j in range(m):
                if a[i + 1][j] == '#':
                    root = dsu.find(num(i + 1, j))
                    if root not in seen:
                        total += counter[root]
                        seen.add(root)
        if i - 1 >= 0:
            for j in range(m):
                if a[i - 1][j] == '#':
                    root = dsu.find(num(i - 1, j))
                    if root not in seen:
                        total += counter[root]
                        seen.add(root)

        for j in range(m):
            if a[i][j] == '#':
                root = dsu.find(num(i, j))
                if root not in seen:
                    total += counter[root]
                    seen.add(root)
            else:
                total += 1

        return total


    def solve_for_col(j: int) -> int:
        total = 0
        seen = set()
        if j + 1 < m:
            for i in range(n):
                if a[i][j + 1] == '#':
                    root = dsu.find(num(i, j + 1))
                    if root not in seen:
                        total += counter[root]
                        seen.add(root)
        if j - 1 >= 0:
            for i in range(n):
                if a[i][j - 1] == '#':
                    root = dsu.find(num(i, j - 1))
                    if root not in seen:
                        total += counter[root]
                        seen.add(root)

        for i in range(n):
            if a[i][j] == '#':
                root = dsu.find(num(i, j))
                if root not in seen:
                    total += counter[root]
                    seen.add(root)
            else:
                total += 1
        return total


    n, m = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append(input())
    dsu = DSU(n * m)
    for j in range(1, m):
        if a[0][j] == '#' and a[0][j - 1] == '#':
            dsu.union(num(0, j), num(0, j - 1))
    for i in range(1, n):
        if a[i][0] == '#' and a[i - 1][0] == '#':
            dsu.union(num(i, 0), num(i - 1, 0))
    for i in range(1, n):
        for j in range(1, m):
            if a[i][j] == '#' and a[i - 1][j] == '#':
                dsu.union(num(i, j), num(i - 1, j))
            if a[i][j] == '#' and a[i][j - 1] == '#':
                dsu.union(num(i, j), num(i, j - 1))
    counter = Counter()
    for k in range(n * m):
        counter[dsu.find(k)] += 1

    best = 0
    for i in range(n):
        cur = solve_for_row(i)
        best = max(best, cur)
    for j in range(m):
        cur = solve_for_col(j)
        best = max(best, cur)
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
