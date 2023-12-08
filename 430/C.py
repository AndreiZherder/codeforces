from collections import defaultdict
from os import path
from sys import stdin, stdout
from types import GeneratorType
from typing import List

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
    def dfs(v: int, par: int, level: int, inverted: List[int]) -> int:
        need_to_invert = init[v] ^ inverted[level % 2] ^ goal[v]
        ans = need_to_invert
        if need_to_invert:
            vs.append(v + 1)
        next_inverted = inverted.copy()
        next_inverted[level % 2] ^= need_to_invert
        for u in g[v]:
            if u != par:
                ans += (yield dfs(u, v, level + 1, next_inverted))
        yield ans

    n = int(input())
    g = defaultdict(list)
    for i in range(n - 1):
        v, u = [int(num) - 1 for num in input().split()]
        g[v].append(u)
        g[u].append(v)
    init = [int(num) for num in input().split()]
    goal = [int(num) for num in input().split()]
    vs = []
    print(dfs(0, -1, 0, [0, 0]))
    print(*vs, sep='\n')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
