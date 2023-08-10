from collections import deque
from os import path
from sys import stdin, stdout


if path.exists("../../templates/input.txt"):
    stdin = open("../../templates/input.txt", 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m, d = [int(num) for num in input().split()]
    g = [[] for i in range(n)]
    mx = 0
    for i in range(m):
        v, u, c = [int(num) for num in input().split()]
        v -= 1
        u -= 1
        g[v].append((u, c))
        mx = max(mx, c)


    """
    FFFFTTTT
        |
    """
    def check(mid: int) -> bool:
        seen = [False for i in range(n)]
        seen[0] = True
        q = deque([(0, 0)])
        while q:
            v, depth = q.popleft()
            if depth < d:
                for u, c in g[v]:
                    if not seen[u]:
                        if c <= mid:
                            if u == n - 1:
                                return True
                            seen[u] = True
                            q.append((u, depth + 1))
        return False

    left = 0
    right = mx
    while left <= right:
        mid = left + (right - left) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1

    if left == mx + 1:
        print(-1)
        return

    seen = [False for i in range(n)]
    par = [-1 for i in range(n)]
    seen[0] = True
    q = deque([0])
    while q:
        v = q.popleft()
        for u, c in g[v]:
            if not seen[u]:
                if c <= left:
                    par[u] = v
                    if u == n - 1:
                        q.clear()
                        break
                    seen[u] = True
                    q.append(u)
    ans = []
    v = n - 1
    while v != -1:
        ans.append(v)
        v = par[v]
    print(len(ans) - 1)
    print(*[v + 1 for v in reversed(ans)])


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
