import sys
from collections import deque
from heapq import heapify, heappop, heappush

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, m = (int(num) for num in input().split())
    p = [int(num) for num in input().split()]
    versions = [0 for i in range(n + m + 1)]
    versions[0] = 10 ** 20
    h = list(zip(reversed(range(1, n + 1)), range(1, n + 1), versions[1:]))
    heapify(h)
    s = set(range(1, n + 1))
    ans = [-1 for i in range(n)]
    for new_time, new_key in enumerate(p, 1):
        if new_key not in s:
            version = 0
            key = 0
            while versions[key] > version:
                t, key, version = heappop(h)
            if key <= n:
                ans[key - 1] = new_time
            s.remove(key)
            versions[new_key] += 1
            heappush(h, (new_time + n, new_key, versions[new_key]))
            s.add(new_key)
        else:
            versions[new_key] += 1
            heappush(h, (new_time + n, new_key, versions[new_key]))
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
