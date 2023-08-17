from os import path
from sys import stdin, stdout
from types import GeneratorType

if path.exists("../templates/input.txt"):
    stdin = open("../templates/input.txt", 'r')


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
        ans[v] = s[v]
        if g[v]:
            for u in g[v]:
                ans[v] += yield dfs(u)
        yield ans[v]

    n = int(input())
    parents = [int(num) for num in input().split()]
    g = [[] for i in range(n)]
    for v, parent in enumerate(parents):
        g[parent - 1].append(v + 1)
    s = [1 if c == 'W' else -1 for c in input()]
    ans = [0 for i in range(n)]
    dfs(0)
    print(ans.count(0))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
