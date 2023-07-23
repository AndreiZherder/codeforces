from collections import defaultdict
from sys import stdin, stdout
from types import GeneratorType


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


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


def solution():
    @bootstrap
    def dfs(v: int) -> bool:
        for u, d in g[v]:
            if u not in seen:
                seen.add(u)
                x[u] = x[v] + d
                if not (yield dfs(u)):
                    yield False
            else:
                if x[u] != x[v] + d:
                    yield False
        yield True

    n, m = [int(num) for num in input().split()]
    g = defaultdict(list)
    for i in range(m):
        v, u, d = [int(num) for num in input().split()]
        g[v].append((u, d))
        g[u].append((v, -d))

    seen = set()
    for v in range(n):
        if v not in seen:
            seen.add(v)
            x = {v: 0}
            if not dfs(v):
                print('NO')
                return
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
