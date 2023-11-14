from collections import defaultdict
from os import path
from sys import stdin, stdout


filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    cost = [int(num) for num in input().split()]
    total = [0 for i in range(n)]
    g = defaultdict(set)
    for i in range(m):
        v, u = [int(num) - 1for num in input().split()]
        g[v].add(u)
        g[u].add(v)
        total[v] += cost[u]
        total[u] += cost[v]
    s = sorted(range(n), key=lambda i: cost[i])
    ans = 0
    while g:
        v = s.pop()
        ans += total[v]
        for u in g[v]:
            total[u] -= cost[v]
            g[u].remove(v)
        del g[v]
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
