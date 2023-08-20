from heapq import heappop, heappush
from typing import List, Tuple
from types import GeneratorType


def input_graph() -> List[List[int]]:
    n, m = (int(num) for num in input().split())
    g = [[] for i in range(n)]
    for i in range(m):
        v, u = (int(num) for num in input().split())
        g[v].append(u)
        g[u].append(v)
    return g


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to
    return wrappedfunc


def toposort(g: List[List[int]]) -> List[int]:
    """
    returns topologically sorted nodes of directed graph
    if graph has cycle, returns empty list
    takes g (adjacency list) as input
    """
    @bootstrap
    def dfs(v: int) -> bool:
        for u in g[v]:
            if color[u] == GREY:
                yield False
            elif color[u] == WHITE:
                color[u] = GREY
                if not (yield dfs(u)):
                    yield False
                color[u] = BLACK
        ans.append(v)
        yield True

    WHITE = 0
    GREY = 1
    BLACK = 2
    n = len(g)
    color = [WHITE for v in range(n)]
    ans = []
    for v in range(n):
        if color[v] == WHITE:
            color[v] = GREY
            if not dfs(v):
                return []
            color[v] = BLACK
    return ans[::-1]


def kahn_toposort(g: List[List[int]]) -> (List[int], bool):
    """
    Kahn topological sort
    returns:
    - topologically sorted nodes of directed graph;
    - acyclicity of graph
    takes g (adjacency list) as input
    """
    n = len(g)
    indeg = [0] * n
    for v in range(n):
        for u in g[v]:
            indeg[u] += 1
    q, ans = [], []
    for v in range(n):
        if indeg[v] == 0:
            q.append(v)
    cnt = 0
    while q:
        v = q.pop()
        ans.append(v)
        cnt += 1
        for u in g[v]:
            indeg[u] -= 1
            if indeg[u] == 0:
                q.append(u)
    acyclicity = cnt == n
    return ans, acyclicity


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


def kruskal(n: int, edges: List[List[int]]):
    """
    Find Minimum Spanning Tree of undirected weighted graph
    """
    dsu = DSU(n)
    edges.sort(key=lambda x: x[2])
    cost = 0
    for u, v, w in edges:
        if dsu.find(u) != dsu.find(v):
            cost += w
            dsu.union(u, v)
    return cost
