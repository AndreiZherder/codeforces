import math

def sieve(n: int):
    nums = [True for i in range(n + 1)]
    p = 2
    while p * p < n + 1:
        if nums[p]:
            for i in range(p * p, n + 1, p):
                nums[i] = False
        p += 1
    for p in range(2, n + 1):
        if nums[p]:
            yield p


def factor(n):
    """
    Prime factors of n.
    # factor(99) --> 3 3 11
    """
    for prime in sieve(math.isqrt(n) + 1):
        while n > 1:
            quotient, remainder = divmod(n, prime)
            if remainder:
                break
            yield prime
            n = quotient
    if n > 1:
        yield n


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
