import sys
from collections import defaultdict
from itertools import accumulate

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, q = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    pref = list(accumulate(a, initial=0))
    while q:
        l, r, k = [int(num) for num in input().split()]
        if (pref[-1] - (pref[r] - pref[l - 1]) + k * (r - l + 1)) % 2 == 1:
            print('YES')
        else:
            print('NO')
        q -= 1


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
