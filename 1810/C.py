import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, c, d = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    a.sort()
    if a[0] != 1:
        cost = n * c + d
        start = 0
    else:
        cost = (n - 1) * c
        start = 1
    waited = 2
    best = cost
    for num in a[start:]:
        if num == waited:
            cost -= c
            best = min(best, cost)
            waited += 1
        elif num > waited:
            best = min(best, cost + c)
            cost += (num - waited) * d - c
            best = min(best, cost)
            waited = num + 1
    print(best)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
