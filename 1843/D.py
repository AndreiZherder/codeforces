import sys
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
    def dfs(v: int) -> int:
        if v == 1:
            for u in g[v]:
                if u not in seen:
                    seen.add(u)
                    cnt[v] += yield dfs(u)
        else:
            if len(g[v]) == 1:
                cnt[v] = 1
            else:
                for u in g[v]:
                    if u not in seen:
                        seen.add(u)
                        cnt[v] += yield dfs(u)
        yield cnt[v]

    n = int(input())
    g = defaultdict(list)
    for i in range(n - 1):
        v, u = (int(num) for num in input().split())
        g[v].append(u)
        g[u].append(v)
    cnt = [0 for i in range(n + 1)]
    seen = {1}
    dfs(1)
    q = int(input())
    for i in range(q):
        x, y = (int(num) for num in input().split())
        print(cnt[x] * cnt[y])


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
