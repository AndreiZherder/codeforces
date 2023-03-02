import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    h = []
    ans = 0
    for num in a:
        if num > 0:
            heappush(h, -num)
        else:
            if h:
                ans += -heappop(h)
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
