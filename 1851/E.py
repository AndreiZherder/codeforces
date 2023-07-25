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
    def dfs(v: int) -> int:
        if v in cache:
            yield cache[v]
        if not g[v]:
            ans = c[v]
        else:
            ans = 0
            for u in g[v]:
                ans += yield dfs(u)
            ans = min(c[v], ans)
        cache[v] = ans
        yield ans


    n, k = [int(num) for num in input().split()]
    c = [int(num) for num in input().split()]
    ps = [int(num) for num in input().split()]
    for i in ps:
        c[i - 1] = 0
    g = defaultdict(list)
    for v in range(n):
        m, *children = [int(num) for num in input().split()]
        g[v] = [u - 1 for u in children]
    ans = []
    cache = dict()
    for v in range(n):
        ans.append(dfs(v))
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
