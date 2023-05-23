import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    g = defaultdict(list)
    for i in range(m):
        v, u = [int(num) for num in input().split()]
        g[v].append(u)
        g[u].append(v)
    leaves = set()
    for node in g:
        if len(g[node]) == 1:
            leaves.add(node)
    parents = set()
    for leaf in leaves:
        parents.add(g[leaf][0])
    y = len(leaves) // len(parents)

    seen = leaves.copy()
    leaves = parents
    parents = set()
    for leaf in leaves:
        for node in g[leaf]:
            if node not in seen:
                parents.add(node)
    x = len(leaves) // len(parents)
    print(x, y)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
