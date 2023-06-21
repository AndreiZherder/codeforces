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
        else:
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
    def dfs(v: int, cur: int) -> int:
        if a[v] == 0:
            cur = 0
        else:
            cur += 1
        if len(g[v]) == 1 and v != 0:
            ans = 1
        else:
            ans = 0
            for u in g[v]:
                if u not in seen:
                    if cur + a[u] <= m:
                        seen.add(u)
                        ans += yield dfs(u, cur)
        yield ans

    n, m = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    g = defaultdict(list)
    for i in range(n - 1):
        v, u = [int(num) for num in input().split()]
        v -= 1
        u -= 1
        g[v].append(u)
        g[u].append(v)
    seen = {0}
    print(dfs(0, 0))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
