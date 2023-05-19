import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


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
    n = int(input())
    a = [int(num) - 1 for num in input().split()]
    dsu = DSU(n)
    for i, num in enumerate(a):
        dsu.union(i, num)
    mx = len({dsu.find(i) for i in range(n)})
    x = 0
    for i in range(n):
        if a[a[i]] == i:
            x += 1
    if x == 0:
        mn = mx
    else:
        mn = mx + 1 - x // 2

    print(mn, mx)



def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
