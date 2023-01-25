from collections import Counter
from heapq import heapify, heappop, heappush


def solution():
    n, m = (int(num) for num in input().split())
    a = [int(num) for num in input().split()]
    c = [int(num) for num in input().split()]
    h = [-v for v in Counter(a).values()]
    heapify(h)
    c.sort(reverse=True)
    ans = 0
    for size in c:
        guests = -heappop(h)
        sit = min(size, guests)
        heappush(h, -(guests - sit))
        ans += sit
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
