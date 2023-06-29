from bisect import bisect_right
from collections import Counter, defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    s = input()
    m = int(input())
    l = input()
    r = input()
    n = len(s)
    best = -1
    for i in range(m):
        start = best + 1
        for j in range(int(l[i]), int(r[i]) + 1):
            pos = start
            while pos < n and int(s[pos]) != j:
                pos += 1
            if pos == n:
                print('YES')
                return
            best = max(best, pos)
    print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
