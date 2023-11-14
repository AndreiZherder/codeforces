from collections import defaultdict
from os import path
from sys import stdin, stdout
from types import GeneratorType

filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


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
    def dfs(v: int, par: int) -> int:
        ans = 0
        if len(g[v]) > 1 or v == 0:
            ans = 0
            for u, t in g[v]:
                if u != par:
                    x = yield dfs(u, v)
                    if x > 0:
                        ans += x
                    elif t == 1:
                        ans += 1
                        a.append(u + 1)
        yield ans

    n = int(input())
    g = defaultdict(list)
    for i in range(n - 1):
        x, y, t = [int(num) - 1 for num in input().split()]
        g[x].append((y, t))
        g[y].append((x, t))
    a = []
    print(dfs(0, -1))
    print(*a)



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
