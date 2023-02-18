import sys
from bisect import bisect_left
from itertools import accumulate

input = sys.stdin.readline


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    ans = [0 for i in range(n)]
    diff = [0 for i in range(n + 1)]
    pref = list(accumulate(b))
    total = 0
    for j, (amount, drink) in enumerate(zip(a, b)):
        i = bisect_left(pref, amount + total)
        if i < n:
            if i >= 1:
                ans[i] += amount + total - pref[i - 1]
            else:
                ans[i] += amount + total
        diff[j] += 1
        diff[i] -= 1
        total += drink
    total = 0
    for i in range(n):
        total += diff[i]
        ans[i] += b[i] * total
    print(*ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
