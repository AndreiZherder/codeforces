import sys
from bisect import bisect_right
from math import sqrt

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    ks = []
    for i in range(n):
        ks.append(int(input()))
    parabolas = []
    for i in range(m):
        parabolas.append([int(num) for num in input().split()])

    ks.sort()
    for a, b, c in parabolas:
        if c < 0:
            print('NO')
        else:
            i = bisect_right(ks, b - 2 * sqrt(a * c))
            if i < n and ks[i] < b + 2 * sqrt(a * c):
                print('YES')
                print(ks[i])
            else:
                print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
