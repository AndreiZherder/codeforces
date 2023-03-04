import sys
from heapq import heapify, heappop, heappush

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    m = []
    cur = 1
    for i in range(n):
        cur = cur * a[n - 1 - i] / (i + 1)
        m.append((-cur, -i - 1, n - 1 - i))
    heapify(m)
    ans = [0 for i in range(n)]
    for k in range(n - 1, -1, -1):
        pos = n
        while pos > k:
            cost, length, pos = heappop(m)
            cost = -cost
            length = -length
        ans[k] = length
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
