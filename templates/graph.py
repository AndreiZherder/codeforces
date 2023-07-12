from typing import List
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
