import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, a, b = [int(num) for num in input().split()]
    g = defaultdict(list)
    for i in range(n - 1):
        u, v, w = [int(num) for num in input().split()]
        g[u].append((v, w))
        g[v].append((u, w))

    vals = set()
    q = deque([(b, 0)])
    seen = {b}
    while q:
        u, x = q.popleft()
        for v, w in g[u]:
            if v not in seen:
                vals.add(x ^ w)
                q.append((v, x ^ w))
                seen.add(v)

    q = deque([(a, 0)])
    seen = {a, b}
    while q:
        u, x = q.popleft()
        if x in vals:
            print('YES')
            return
        for v, w in g[u]:
            if v not in seen:
                q.append((v, x ^ w))
                seen.add(v)
    print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
