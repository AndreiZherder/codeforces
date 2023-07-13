from heapq import heappop, heappush
from sys import stdin, stdout
from typing import List, Tuple


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    def dijkstra(g: List[List[Tuple[int, int]]], start: int):
        """
        Uses Dijkstra's algortihm to find the shortest path from node start
        to all other nodes in a directed weighted graph.
        """
        n = len(g)
        dist, parent = [10 ** 20] * n, [-1] * n
        dist[start] = 0

        q = [(0, start)]
        while q:
            cur, v = heappop(q)
            if cur == dist[v]:
                for u, w in g[v]:
                    if cur + w < dist[u]:
                        dist[u], parent[u] = cur + w, v
                        heappush(q, (cur + w, u))
        return dist, parent

    n, m = [int(num) for num in input().split()]
    n = 2 ** n
    g = [[] for i in range(n)]
    start = int(input(), 2)
    for j in range(m):
        w = int(input())
        andmask = int(input(), 2)
        ormask = int(input(), 2)
        for v in range(n):
            g[v].append((v & ~andmask | ormask, w))
    ans, _ = dijkstra(g, start)
    if ans[0] != 10 ** 20:
        print(ans[0])
    else:
        print(-1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
